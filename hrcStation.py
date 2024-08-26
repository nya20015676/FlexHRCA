import random
from matplotlib import pyplot as plt
import numpy as np
import gantt_HRC as gt
import itertools
from scipy.stats import norm, nbinom
from fuzzyNumber import FuzzyNumber, SVTNN
import time
from multiprocessing.pool import Pool
import copy

class Human:
    # Properties
    name = "undefined"
    gender = "undefined"
    height = 170
    weight = 70

    # metrics for human
    fatigue = 0
    workTime = 0
    finishedOpNum = 0
    ngOpNum = 0
    ngRate = 0
    finishedProductsNum = 0
    
    capability = 5 # 1~10
    cost = 10000
    # op related
    finishedOpNumOfScrew = 0
    finishedOpNumOfWiring = 0

    def __init__(self, name, capability = 5):
        self.name = name
        self.capability = capability
        self.cost = self.cost + 10000*capability

    def calculate_time(self, intensity):
        return int(intensity * self.capability / 2)

class Robot:
    # Properties
    name = "undefine"
    serialNumber = "undefine"
    model = "undefine"
    cost = 100000
    capability = 5

    # Metrics for cobot
    # Testable metrics


    # realtime variables on each op
    trajectory = {"terminal":[], "axis1":[], "axis2":[], "axis3":[],"axis4":[],"axis5":[],"axis6":[]}


    def __init__(self, name, capability = 5):
        self.name = name
        self.capability = capability

    def calculate_time(self, intensity):
        return int(intensity * self.capability / 3)

class Productt:
    name = "undefine"
    quantity = 0
    def __init__(self, name="undefine"):
        self.name = name

    
    def set_jobs(self, n_job_op, after_require):
        # n_job_op: dictionary {IdxofJob:IdxofOp, 0:3, 1:4 ... }
        # after_require: size is n_op, if there is no order requirement, it is [], if there is, all pre-requirements are represented by a list, e.g. [0,1] means it needs to be after O11 and O12
        # [[0], [1]，[1]]
        self.n_job = max(n_job_op.keys()) + 1
        self.n_op = sum(n_job_op.values())
        self.n_job_op = copy.deepcopy(n_job_op)
        self.after_require = copy.deepcopy(after_require)

    def add_product(self, product):
        n_job_op = product.n_job_op
        after_require = product.after_require
        new_n_job_op = {job + self.n_job: op for job, op in n_job_op.items()}
        new_after_require = [[num + self.n_op for num in sublist] if sublist else sublist for sublist in after_require]
        self.n_job_op.update(new_n_job_op)
        self.after_require += new_after_require
        self.n_job = max(self.n_job_op.keys()) + 1
        self.n_op = sum(self.n_job_op.values())


        
class HrcStation:
    def __init__(self):
        pass

    def random_MSOS(self): 
    # The H and R numbers start from 0
        MS, OS = [], []
        for i in range(self.product.n_op):
            indices = [i for i, x in enumerate(self.Time[i]) if x != 9999]
            MS.append(random.choice(indices))
                    
        for i in range(self.product.n_op):
            candidate_list = []
            for j, after_list in enumerate(self.product.after_require):
                    # if after_list all in OS:
                    if j in OS:
                        continue
                    if set(after_list).issubset(set(OS)):
                        candidate_list.append(j)
            OS.append(random.choice(candidate_list))
        return MS, OS
    
    def Time_idx_to_hr_1xx(self, idx):
        # pos_H_n = (min_index - self.n_human - self.n_robot + 1)//self.n_robot-1
        # pos_R_m = min_index - pos_H_n*self.n_robot - self.n_robot - self.n_human + 2

        #     H1 H2 R1 R2 R3 H1&R1 H1&R2 H1&R3 H2&R1 H2&R2 H2&R3
        # O11 t  t  ...
        # O12
        # ...
        pos_H_n = (idx+1 - self.n_human - self.n_robot-1) // self.n_robot
        pos_R_m = (idx+1 - self.n_human - self.n_robot-1) % self.n_robot + self.n_human
        
        xxx = 100 + pos_H_n*10 + pos_R_m
        return xxx

    def hr_1xx_to_Time_idx(self, xxx):
        pos_H_n = int((xxx-100) / 10)+1 
        pos_R_m = int((xxx-100) % 10)+1
        n_H = pos_H_n 
        n_R= pos_R_m - self.n_human 
        index = self.n_human + self.n_robot + (self.n_robot*(n_H-1)+n_R) -1
        return index

    def set_operator_product_Time(self, human_list, robot_list, product_list, Time_list):
    
    # Time:
    #     H1 H2 R1 R2 R3 H1&R1 H1&R2 H1&R3 H2&R1 H2&R2 H2&R3
    # O11 t  t  9999
    # O12
    # ...
        for t in Time_list[0][0]:
            if t != 9999:
                self.TIMETYPE = type(t)
        self.n_human = len(human_list)
        self.n_robot = len(robot_list)
        self.human_list = copy.deepcopy(human_list)
        self.robot_list = copy.deepcopy(robot_list)
        self.product = product_list[0]
        for i, p in enumerate(product_list):
            if i <1:
                continue
            self.product.add_product(p)
        self.Time = copy.deepcopy(Time_list[0])
        for i, t in enumerate(Time_list):
            if i <1:
                continue
            self.Time += Time_list[i]

    def print_matrix(_, row_labels, col_labels, arr):
        max_row_label_len = max(len(label) for label in row_labels) if row_labels else 0
        max_col_label_len = max(len(label) for label in col_labels) if col_labels else 0

        if col_labels:
            print(" " * (max_row_label_len + 1), end="\t")

            for col_label in col_labels:
                print(col_label.ljust(max_col_label_len), end="\t")
            print()  

        for i in range(len(arr)):
            if row_labels and i < len(row_labels):
                print(row_labels[i].ljust(max_row_label_len), end="\t")
            else:
                print(" " * max_row_label_len, end="\t")

            for j in range(len(arr[i])):
                print(str(arr[i][j]).ljust(max_col_label_len), end="\t")
            print()  
    
    def gantt(self, OS_COS_MS_TS_START_END_AFTER):
        # custom_packages = [
        #     {"start": 0.0, "end": 1.0, "machine": 5, "job": 8},
        #     {"start": 0.0, "end": 4.0, "machine": 2, "job": 0},
        # ]
        custom_packages = []
        for op in OS_COS_MS_TS_START_END_AFTER:
            if op[2] < 100:
                custom_packages.append({"start":op[4], "end":op[5], "machine": op[2], "job":op[0]})
            else:
                pos_H_n = int((op[2]-100) / 10) 
                pos_R_m = int((op[2]-100) % 10)
                custom_packages.append({"start":op[4], "end":op[5], "machine": pos_H_n, "job":op[0]})
                custom_packages.append({"start":op[4], "end":op[5], "machine": pos_R_m, "job":op[0]})
        
        data = {
            "machines": self.n_human+self.n_robot,
            "jobs": self.product.n_job,
            "xlabel": "time",
            "title": "gantt",
            "packages": custom_packages
        }
        gt.gantt(data)

    def gantt_HRC(self, OS_COS_MS_TS_START_END_AFTER):
        # custom_packages = [
        #     {"start_low":0, "start": 0.0, "start_up":0, "end_low":1, "end": 1, "end_up":1, "machine": 5, "job": 8},
        #     {"start_low":0, "start": 0.0, "start_up":0, "end_low":4, "end": 4, "end_up":4, "machine": 2, "job": 1},
        # ]
        custom_packages = []
        for op in OS_COS_MS_TS_START_END_AFTER:
            if op[2] < self.n_human+self.n_robot:
                idx = op[2]
                if idx < self.n_human:
                    machine = "Human" + str(idx+1)
                else:
                    machine = "Robot" + str(idx+1 - self.n_human)
                custom_packages.append({"start_low":op[4].low if type(op[4])==FuzzyNumber else op[4], "start":op[4].mean if type(op[4])==FuzzyNumber else op[4], "start_up":op[4].up if type(op[4])==FuzzyNumber else op[4], "end_low":op[5].low if type(op[5])==FuzzyNumber else op[5], "end":op[5].mean if type(op[5])==FuzzyNumber else op[5], "end_up":op[5].up if type(op[5])==FuzzyNumber else op[5], "machine": machine, "job":op[0]+1})
            else:
                Time_index = op[2]
                xxx = self.Time_idx_to_hr_1xx(Time_index)
                pos_H_n = int((xxx-100) / 10) 
                pos_R_m = int((xxx-100) % 10)
                machine_H = "Human" + str(pos_H_n+1)
                machine_R = "Robot" + str(pos_R_m+1-self.n_human)
                custom_packages.append({"start_low":op[4].low if type(op[4])==FuzzyNumber else op[4], "start":op[4].mean if type(op[4])==FuzzyNumber else op[4], "start_up":op[4].up if type(op[4])==FuzzyNumber else op[4], "end_low":op[5].low if type(op[5])==FuzzyNumber else op[5], "end":op[5].mean if type(op[5])==FuzzyNumber else op[5], "end_up":op[5].up if type(op[5])==FuzzyNumber else op[5], "machine": machine_H, "job":op[0]+1})
                custom_packages.append({"start_low":op[4].low if type(op[4])==FuzzyNumber else op[4], "start":op[4].mean if type(op[4])==FuzzyNumber else op[4], "start_up":op[4].up if type(op[4])==FuzzyNumber else op[4], "end_low":op[5].low if type(op[5])==FuzzyNumber else op[5], "end":op[5].mean if type(op[5])==FuzzyNumber else op[5], "end_up":op[5].up if type(op[5])==FuzzyNumber else op[5], "machine": machine_R, "job":op[0]+1})

        
        data = {
            "machines": self.n_human+self.n_robot,
            "jobs": self.product.n_op,
            "xlabel": "time",
            "title": "gantt",
            "packages": custom_packages
        }
        gt.gantt_HRC(data)

    def insert_operator(self, op_time_start, op_time_end, op_time, after):
        # [0 2 0 10 ]
        # [0 5 0 20 ]
        # return start_time, end_time, ok_spare_time_list:[[0, start0], [end0, start1],[latest_end, 9999]]
            # op_time_list:[[start0, end0], [start1, end1]...]
            op_time_list = []
            for i in range(len(op_time_start)):
                if op_time_end[i] > 0: # There is op processing
                    op_time_list.append([op_time_start[i], op_time_end[i]])
                    
            # If the operator does not have OP
            if op_time_list == []: 
                return after, after+op_time, [[after, 9999]]
            
            # Sort the processing time periods from smallest to largest starting time
            op_time_list = sorted(op_time_list, key=lambda x: x[0]) 

            # Calculate the gap of OP
            # If there is only one OP, determine whether to start from 0 and insert the gap [0, start0]
            # spare_time_list:[[0, start0], [end0, start1], [latest_end, 9999]]
            spare_time_list = [[0, op_time_list[0][0]]] if op_time_list[0][0] > 0 else []

            # If the machine has more than one OP, insert a gap [end0, start1]
            if len(op_time_list) > 1: 
                for i in range(1, len(op_time_list)):
                    if op_time_list[i][0] > op_time_list[i-1][1]:
                        spare_time_list.append([op_time_list[i-1][1], op_time_list[i][0]])

            # Insert at the end [latest_end, 9999]
            spare_time_list.append([op_time_list[-1][1], 9999])

            # If there is no free gap, OP is sorted backward
            # if spare_time_list == []: 
            #     time_start = after if after > op_time_list[-1][1] else op_time_list[-1][1]
            #     time_end = time_start + op_time
            #     return time_start, time_end, [[op_time_list[0][1], 9999]]

            # Determine which gaps are OK
            ok_spare_time_list = []
            for time in spare_time_list:
                if time[1] < op_time + time[0]:
                    continue
                # elif time[1] - after >= op_time:
                elif time[1]  > op_time + after:
                    ok_spare_time_list.append(time)
            
            # No gap inserted
            ok_spare_time_list = [ok_spare_time_list[-1]]

            # If there is no gap, it is OK, OP will sort it later.
            # if ok_spare_time_list == []: 
            #     time_start = after if after > op_time_list[-1][1] else op_time_list[-1][1]
            #     time_end = time_start + op_time
            #     return time_start, time_end, ok_spare_time_list
            
            # If there are multiple OK gaps, insert the gap with the earliest time.
            # ok_spare_time_list[0][0] = after if after > ok_spare_time_list[0][0] else ok_spare_time_list[0][0]
            ok_spare_time_list[0][0] = self.TIMETYPE.maximum([after, ok_spare_time_list[0][0]]) if isinstance(after, FuzzyNumber) or isinstance(ok_spare_time_list[0][0], FuzzyNumber) else max(after, ok_spare_time_list[0][0])
            time_start = ok_spare_time_list[0][0]
            time_end = time_start + op_time
            return time_start, time_end, ok_spare_time_list

            # If there are multiple OK gaps, insert the one with the shortest time.
            # min_ok_spare_time = min(ok_spare_time_list, key=lambda x: x[1] - x[0])
            # time_start = after if after > min_ok_spare_time[0] else min_ok_spare_time[0]
            # time_end = time_start + op_time
            # return time_start, time_end

    def decoding_MSOS(self, MS, OS):
        TMS = []
        for n_operator, i in zip(MS, range(len(MS))):
            TMS.append(self.Time[i][n_operator])

        # after_require = [ # 0~8
                #             [], [0], [0], [0], [0], [0], [0], [0], [0],
                #           # 9~17
                #             [], [9], [9], [9], [9], [9], [9], [9], [9],
                #           # 18~22
                #             [], [18], [18], [18], [18],
                #             [], [23], [23], [23], [23],
                #             [0,1,2,3,4,5,6,7,8] ]

        # [0, 3, 1, 4, 9, 15, 14, 23, 24, 10, 27, 8, 2, 16, 13, 6, 7, 17, 25, 11, 12, 5, 26, 18, 21, 19, 22, 20, 28]
        # [9, 23, 13, 25, 26, 18, 10, 27, 0, 2, 24, 1, 4, 14, 21, 11, 6, 22, 17, 19, 16, 3, 7, 15, 20, 5, 8, 12, 28]

        MOS = []
        TOS = []
        COS = []
        count_dict = {}
        for i, op in enumerate(OS):
            MOS.append(MS[op])
            TOS.append(TMS[op])
            COS.append(0)

        # job op machine time relationship
        # OS_COS_MS_TS_START_END_AFTER[i][0],OS_COS_MS_TS_START_END_AFTER[i][1]Indicates the NumofJob, NumofOp represented by the i-th element in OS
        # OS_COS_MS_TS_START_END_AFTER[i][2] Op's operator number
        # OS_COS_MS_TS_START_END_AFTER[i][3] Op process time
        # OS_COS_MS_TS_START_END_AFTER[i][4]~[5] Op start and end time
        # OS_COS_MS_TS_START_END_AFTER[i][6] after_require's preceding OP end time
        OS_COS_MS_TS_START_END_AFTER = [[0 for _ in range(7)] for _ in range(len(OS))]
        for i in range(len(OS)):
            OS_COS_MS_TS_START_END_AFTER[i][0] = OS[i]
            OS_COS_MS_TS_START_END_AFTER[i][1] = COS[i]
            OS_COS_MS_TS_START_END_AFTER[i][2] = MOS[i]
            OS_COS_MS_TS_START_END_AFTER[i][3] = TOS[i]
            
        
        # start_time
        # H1   [ 0  0  0  0 20  0  0  0 32]
        # H2   [ 0  0  0  0 22  0  0  0 32]
        # R1   [ 0 22  0 14  0 32 10  0  0]
        # R2   [ 0 22  0 14  0 32 10  0  0]
        # R3   [ 0 22  0 14  0 32 10  0  0]
        # end_time
        # H1   [ 0 10  0  0 22  0  0  0 36]
        # H2   [ 0  0  0  0 22  0  0  0 36]
        # R1   [ 0 22  0 14  0 32 10  0  0]
        # R2   [ 0 22  0 14  0 32 10  0  0]
        # R3   [ 0 22  0 14  0 32 10  0  0]
        shape = (self.n_human+self.n_robot, len(OS))
        TMOS_start = [[0] * shape[1] for _ in range(shape[0])]
        TMOS_end = [[0] * shape[1] for _ in range(shape[0])]
        # [[0, 0, 0, 30], [3, 0, 2, 15], [2, 0, 2, 15], [2, 1, 102, 62], [0, 1, 1, 24] ...
        # [[OS, COS, MOS, TOS, start_time, end_time]]
        for op, i in zip(OS_COS_MS_TS_START_END_AFTER, range(len(OS_COS_MS_TS_START_END_AFTER))):
            one_op_start_time = time.time()
            last_end = 0
            # If OP is the first step of the job
            if op[1] == 0: 
                last_end = 0

            if self.product.after_require[OS[i]] != []:
                # Find the index of all the predecessor OPs of this OP in this OS
                after_index_list = list(OS.index(n) for n in self.product.after_require[OS[i]] if n in OS)
            else:
                after_index_list = []
            op[6] = max(list(OS_COS_MS_TS_START_END_AFTER[index][5] for index in after_index_list)) if after_index_list != [] else 0
            last_end = max(last_end, op[6])

            one_op_before_insert_time = time.time()
            before_insert_long = one_op_before_insert_time - one_op_start_time
            #print("time one op before_insert: ", before_insert_long)

            insert_once_long = 0
            insert_twice_long = 0
            # If the OP is not H&R
            if op[2] < self.n_human+self.n_robot:
                start, end, _ = self.insert_operator(TMOS_start[op[2]], TMOS_end[op[2]], op[3], last_end)
                TMOS_start[op[2]][i] = start
                TMOS_end[op[2]][i] = end
                op[4] = start
                op[5] = end
                one_op_after_insert_time = time.time()
                insert_once_long = one_op_after_insert_time - one_op_before_insert_time
                #print("time one op after_insert ONCE: ", insert_once_long)
            

            # If is H&R
            else:
                Time_index = op[2]
                xxx = self.Time_idx_to_hr_1xx(Time_index)
                pos_H_n = int((xxx-100) / 10) 
                pos_R_m = int((xxx-100) % 10)
                H_start, H_end, H_ok_spare_time_list = self.insert_operator(TMOS_start[pos_H_n], TMOS_end[pos_H_n], op[3], last_end)
                R_start, R_end, R_ok_spare_time_list = self.insert_operator(TMOS_start[pos_R_m], TMOS_end[pos_R_m], op[3], last_end)
                one_op_after_insert_time = time.time()
                insert_twice_long = one_op_after_insert_time - one_op_before_insert_time
                
                def find_time_overlap(array1, array2):
                    def find_overlap(interval1, interval2):
                        start1, end1 = interval1
                        start2, end2 = interval2
                        overlap_start = max(start1, start2)
                        overlap_end = min(end1, end2)
                        if overlap_start < overlap_end:
                            return [overlap_start, overlap_end]
                        else:
                            return None
                    overlaps = []
                    for interval1 in array1:
                        for interval2 in array2:
                            overlap = find_overlap(interval1, interval2)
                            if overlap:
                                overlaps.append(overlap)
                    return overlaps

                overlaps = find_time_overlap(H_ok_spare_time_list, R_ok_spare_time_list)
                for overlap in overlaps:
                    # if overlap[1] - overlap[0] >= op[3]:
                    if overlap[1] > op[3] + overlap[0]:
                        start = overlap[0]
                        end = start + op[3]
                        TMOS_start[pos_H_n][i] = start
                        TMOS_end[pos_H_n][i] = end
                        TMOS_start[pos_R_m][i] = start
                        TMOS_end[pos_R_m][i] = end
                        op[4] = start
                        op[5] = end
                        break
            one_op_end_time = time.time()
            one_op_long = one_op_end_time - one_op_start_time
            # print("time one op:{:.3f},  before_insert_long:{:.3f}/{:.2f}%, insert_once_long:{:.3f}/{:.2f}%, insert_twice_long:{:.3f}/{:.2f}%".format( 
            #       one_op_long, before_insert_long, before_insert_long/one_op_long*100 if one_op_long>0 else 0, insert_once_long, insert_once_long/one_op_long*100 if one_op_long>0 else 0, insert_twice_long, insert_twice_long/one_op_long*100 if one_op_long>0 else 0))

        TMOS = [TMOS_start, TMOS_end]
        return OS_COS_MS_TS_START_END_AFTER, TMOS
    
    def calculate_fitness_parallel(self, chs):
        return self.calculate_fitness(chs[0], chs[1])
    def calculate_fitness(self, MS, OS):
        _, TMOS = self.decoding_MSOS(MS, OS)
        end_time_list = list(max(row) for row in TMOS[1])
        if any(isinstance(x, FuzzyNumber) for x in end_time_list):
            return self.TIMETYPE.maximum(end_time_list)
        else:
            return max(end_time_list)
            
        

    def crossover_MS(self, P_MS1, P_MS2):
        T = len(P_MS1)
        C_MS1 = [None] * T
        C_MS2 = [None] * T
        for i in range(T):
            if random.random() < 0.5:  # randomly select from parent 1
                C_MS1[i] = P_MS1[i]
                C_MS2[i] = P_MS2[i]
            else:  # randomly select from parent 2
                C_MS1[i] = P_MS2[i]
                C_MS2[i] = P_MS1[i]
        return C_MS1, C_MS2

    def crossover_OS(self, P_OS1, P_OS2):
        # For OS, POX crosses P_OS1 line crosses P_OS2, and then crosses vice versa.
        J_num = self.product.n_op
        Job_list = [i for i in range(J_num)]
        random.shuffle(Job_list)
        r = random.randint(1, J_num - 1)
        Set1 = Job_list[0:r]
        Set2 = Job_list[r:J_num]
        T0 = self.product.n_op
        new_os = list(np.zeros(T0, dtype=int))
        new_os2 = list(np.zeros(T0, dtype=int))
        for k, v in enumerate(P_OS1):
            if v in Set1:
                new_os[k] = v + 1
        for i in P_OS2:
            if i not in Set1:
                Site = new_os.index(0)
                new_os[Site] = i + 1

        for k, v in enumerate(P_OS2):
            if v in Set1:
                new_os2[k] = v + 1
        for i in P_OS1:
            if i not in Set1:
                Site = new_os2.index(0)
                new_os2[Site] = i + 1
        new_os = [j - 1 for j in new_os]
        new_os2 = [j - 1 for j in new_os2]
        
        C_OS1, C_OS2 = new_os, new_os2

         # after_require = [ # 0~8
                #             [], [0], [0], [0], [0], [0], [0], [0], [0],
                #           # 9~17
                #             [], [9], [9], [9], [9], [9], [9], [9], [9],
                #           # 18~22
                #             [], [18], [18], [18], [18],
                #             [], [23], [23], [23], [23],
                #             [0,1,2,3,4,5,6,7,8] ]

        # [0, 3, 1, 4, 9, 15, 14, 23, 24, 10, 27, 8, 2, 16, 13, 6, 7, 17, 25, 11, 12, 5, 26, 18, 21, 19, 22, 20, 28]
        # [9, 23, 13, 25, 26, 18, 10, 27, 0, 2, 24, 1, 4, 14, 21, 11, 6, 22, 17, 19, 16, 3, 7, 15, 20, 5, 8, 12, 28]
        for i, opNum in enumerate(C_OS1):
            after_list_of_the_op = self.product.after_require[opNum]
            if after_list_of_the_op != []:
                after_index = max(C_OS1.index(n) for n in after_list_of_the_op if n in C_OS1)
                if after_index > i:
                    C_OS1[i], C_OS1[after_index] = C_OS1[after_index], C_OS1[i]
        for i, opNum in enumerate(C_OS2):
            after_list_of_the_op = self.product.after_require[opNum]
            if after_list_of_the_op != []:
                after_index = max(C_OS2.index(n) for n in after_list_of_the_op if n in C_OS2)
                if after_index > i:
                    C_OS2[i], C_OS2[after_index] = C_OS2[after_index], C_OS2[i]

        return C_OS1, C_OS2
    
    def variation_MS(self, MS):
        # During the variation process, the machine with the best processing time will be selected
        T0 = self.product.n_op
        Tr=[i_num for i_num in range(T0)]
        new_MS = list(MS)
        r = random.randint(1, T0 - 1)  # Select r positions in the mutant chromosome
        random.shuffle(Tr)
        # [0 3 4 7]
        T_r = Tr[0:r]
        for i in T_r:
            machine_time = []
            for time in self.Time[i]:
                machine_time.append(time)
            min_index = machine_time.index(min(machine_time))
            # If H&R
            if MS[i] >= 100:
                new_MS[i] = self.Time_idx_to_hr_1xx(min_index)
            else:
                new_MS[i] = min_index
        return new_MS
    
    def variation_OS_return_optimal_one(self, MS, OS):
        one_os_mutate_start = time.time()
        J_num = self.product.n_op
        new_OS=list(OS)
        r=random.randint(1,J_num-1)
        r = min(r, 4)
        Tr=[i for i in range(J_num)]
        random.shuffle(Tr)
        Tr=Tr[0:r]
        J_os=dict(enumerate(new_OS))    
        J_os = sorted(J_os.items(), key=lambda d: d[1])
        Site=[]
        for i in range(r):
            Site.append(new_OS.index(Tr[i])) 
        A=list(itertools.permutations(Tr, r))
        A_OS=[]
        for i in range(len(A)):
            for j in range(len(A[i])):
                new_OS[Site[j]]=A[i][j]
            A_OS.append(list(new_OS))

        # after_require = [ # 0~8
                #             [], [0], [0], [0], [0], [0], [0], [0], [0],
                #           # 9~17
                #             [], [9], [9], [9], [9], [9], [9], [9], [9],
                #           # 18~22
                #             [], [18], [18], [18], [18],
                #             [], [23], [23], [23], [23],
                #             [0,1,2,3,4,5,6,7,8] ]

        # [0, 3, 1, 4, 9, 15, 14, 23, 24, 10, 27, 8, 2, 16, 13, 6, 7, 17, 25, 11, 12, 5, 26, 18, 21, 19, 22, 20, 28]
        # [9, 23, 13, 25, 26, 18, 10, 27, 0, 2, 24, 1, 4, 14, 21, 11, 6, 22, 17, 19, 16, 3, 7, 15, 20, 5, 8, 12, 28]
        new_A_OS = []
        for i, os in enumerate(A_OS):
            should_remove = False
            for j, opNum in enumerate(os):
                after_list_of_the_op = self.product.after_require[opNum]
                if after_list_of_the_op != []:
                    after_index = max(os.index(n) for n in after_list_of_the_op if n in os)
                    if after_index > j:
                        should_remove = True
                        break
            if not should_remove:
                new_A_OS.append(os)

        Fit = []
        one_os_mutate_before_fitness = time.time()
        for os in new_A_OS:
            Fit.append(self.calculate_fitness(MS, os))
        one_os_mutate_after_fitness = time.time()
        fitness_all_time = one_os_mutate_after_fitness - one_os_mutate_before_fitness
        #print("time r=", r)

        one_os_mutate_before_recur = time.time()
        if Fit == []:
            return self.variation_OS_return_optimal_one(MS, OS)
        index_of_new_AOS = Fit.index(min(Fit))
        one_os_mutate_after_recur  = time.time()
        recur_time = one_os_mutate_after_recur - one_os_mutate_before_recur
        one_os_mutate_end = time.time()
        one_os_time = one_os_mutate_end - one_os_mutate_start
        #print("time before_fitnes:{:.3f}, fitness_all_time:{:.3f}/{:.2f}%, recur_time:{:.3f}/{:.2f}%".format(
            # one_os_mutate_before_fitness-one_os_mutate_start, fitness_all_time, fitness_all_time/one_os_time*100 if one_os_time !=0 else 0, recur_time, recur_time/one_os_time*100 if one_os_time !=0 else 0))
        return new_A_OS[index_of_new_AOS]

    def variation_OS_return_random_one(self, MS, OS):
        one_os_mutate_start = time.time()
        J_num = self.product.n_op
        new_OS=list(OS)
        r=random.randint(1,J_num-1)
        r = min(r, 4)
        Tr=[i for i in range(J_num)]
        random.shuffle(Tr)
        Tr=Tr[0:r]
        J_os=dict(enumerate(new_OS))    
        J_os = sorted(J_os.items(), key=lambda d: d[1])
        Site=[]
        for i in range(r):
            Site.append(new_OS.index(Tr[i])) 
        A=list(itertools.permutations(Tr, r))
        A_OS=[]
        for i in range(len(A)):
            for j in range(len(A[i])):
                new_OS[Site[j]]=A[i][j]
            A_OS.append(list(new_OS))

        # after_require = [ # 0~8
                #             [], [0], [0], [0], [0], [0], [0], [0], [0],
                #           # 9~17
                #             [], [9], [9], [9], [9], [9], [9], [9], [9],
                #           # 18~22
                #             [], [18], [18], [18], [18],
                #             [], [23], [23], [23], [23],
                #             [0,1,2,3,4,5,6,7,8] ]

        # [0, 3, 1, 4, 9, 15, 14, 23, 24, 10, 27, 8, 2, 16, 13, 6, 7, 17, 25, 11, 12, 5, 26, 18, 21, 19, 22, 20, 28]
        # [9, 23, 13, 25, 26, 18, 10, 27, 0, 2, 24, 1, 4, 14, 21, 11, 6, 22, 17, 19, 16, 3, 7, 15, 20, 5, 8, 12, 28]
        new_A_OS = []
        for i, os in enumerate(A_OS):
            should_remove = False
            for j, opNum in enumerate(os):
                after_list_of_the_op = self.product.after_require[opNum]
                if after_list_of_the_op != []:
                    after_index = max(os.index(n) for n in after_list_of_the_op if n in os)
                    if after_index > j:
                        should_remove = True
                        break
            if not should_remove:
                new_A_OS.append(os)

        if new_A_OS == []:
            return self.variation_OS_return_random_one(MS, OS)
        return random.choice(new_A_OS)

    def variation_OS_return_random_multi(self, MS, OS):
        one_os_mutate_start = time.time()
        J_num = self.product.n_op
        new_OS=list(OS)
        r=random.randint(1,J_num-1)
        r = min(r, 6)
        Tr=[i for i in range(J_num)]
        random.shuffle(Tr)
        Tr=Tr[0:r]
        J_os=dict(enumerate(new_OS))    
        J_os = sorted(J_os.items(), key=lambda d: d[1])
        Site=[]
        for i in range(r):
            Site.append(new_OS.index(Tr[i]))
        A=list(itertools.permutations(Tr, r))
        A_OS=[]
        for i in range(len(A)):
            for j in range(len(A[i])):
                new_OS[Site[j]]=A[i][j]
            A_OS.append(list(new_OS))

        # after_require = [ # 0~8
                #             [], [0], [0], [0], [0], [0], [0], [0], [0],
                #           # 9~17
                #             [], [9], [9], [9], [9], [9], [9], [9], [9],
                #           # 18~22
                #             [], [18], [18], [18], [18],
                #             [], [23], [23], [23], [23],
                #             [0,1,2,3,4,5,6,7,8] ]

        # [0, 3, 1, 4, 9, 15, 14, 23, 24, 10, 27, 8, 2, 16, 13, 6, 7, 17, 25, 11, 12, 5, 26, 18, 21, 19, 22, 20, 28]
        # [9, 23, 13, 25, 26, 18, 10, 27, 0, 2, 24, 1, 4, 14, 21, 11, 6, 22, 17, 19, 16, 3, 7, 15, 20, 5, 8, 12, 28]
        new_A_OS = []
        for i, os in enumerate(A_OS):
            should_remove = False
            for j, opNum in enumerate(os):
                after_list_of_the_op = self.product.after_require[opNum]
                if after_list_of_the_op != []:
                    after_index = max(os.index(n) for n in after_list_of_the_op if n in os)
                    if after_index > j:
                        should_remove = True
                        break
            if not should_remove:
                new_A_OS.append(os)

        one_os_mutate_before_recur = time.time()
        if new_A_OS == []:
            return self.variation_OS_return_random_multi(MS, OS)
        # index_of_new_AOS = Fit.index(min(Fit))
        one_os_mutate_after_recur  = time.time()
        recur_time = one_os_mutate_after_recur - one_os_mutate_before_recur
        one_os_mutate_end = time.time()
        one_os_time = one_os_mutate_end - one_os_mutate_start
        #print("time before_fitnes:{:.3f}, fitness_all_time:{:.3f}/{:.2f}%, recur_time:{:.3f}/{:.2f}%".format(
            # one_os_mutate_before_fitness-one_os_mutate_start, fitness_all_time, fitness_all_time/one_os_time*100 if one_os_time !=0 else 0, recur_time, recur_time/one_os_time*100 if one_os_time !=0 else 0))
        return new_A_OS

    def select_tournament(self, offspring, size, k):
        # calculate_fitness is performed during selection to calculate the fitness of fewer populations and improve the algorithm speed
        # Randomly select k elements each time, select the smallest one, and loop until enough size elements are selected.
        selected = []
        fitness_selected = []
        pop = []
        fitness_pop = []
        for _ in range(size):
            random_selection = random.choices(offspring, k=k)
            selected += random_selection

        # Single thread
        for chs in selected:
            fitness_selected.append(self.calculate_fitness(chs[0], chs[1]))
        # Multi thread
        # pool = Pool(5)
        # fitness_selected = pool.map(self.calculate_fitness_parallel, selected)
        # pool.close()
        # pool.join()

        for i in range(0, len(selected), k): 
            sublist_fitness = fitness_selected[i:i+k]
            index = sublist_fitness.index(min(sublist_fitness)) + i
            pop.append(selected[index])
            fitness_pop.append(fitness_selected[index])
        return pop, fitness_pop


    def GA_initialed_pop(self, pop, pop_size, p_crossover, p_cross_machine, p_mutation, p_mutation_machine, max_iteration, tSize=3):
        offspring = []
        optimal_fitness = 9999 
        memory_CHS_list = [] 
        memory_CHS_fitness_list = [] 
        optimal_CHS_list = [] 
        best_fitness_list = [] 
        record_list = [] 
        one_iteration_time = 0
        iteration_start_time = time.time()
        for i in range(max_iteration):
            cal_pop_fitness_time = 0
            select_time = 0
            crossover_MS_time = 0
            crossover_OS_time = 0
            mutate_MS_time = 0
            mutate_OS_time = 0
            cal_fitness_start = time.time()

            fitness_pop = []
            if i==0: 
                for chs in pop:
                    fitness_pop.append(self.calculate_fitness(chs[0], chs[1]))
                # pool = Pool()
                # fitness_pop = pool.map(self.calculate_fitness_parallel, pop)
                # pool.close()
                # pool.join()

                memory_CHS_list = list(pop)
                memory_CHS_fitness_list = list(fitness_pop)
                combined_list = list(zip(memory_CHS_list, memory_CHS_fitness_list))
                sorted_combined_list = sorted(combined_list, key=lambda x: x[1])
                memory_CHS_list = [item[0] for item in sorted_combined_list]
                memory_CHS_fitness_list = [item[1] for item in sorted_combined_list]
            else: 
                # Select
                select_start = time.time()
                pop, fitness_pop = self.select_tournament(offspring, pop_size, tSize)
                select_time = time.time() - select_start

                # If the objective function value is the same as the best one in the memory bank, compare the Hamming distance of the machine selection part. If it is zero, do not replace it; if it is not zero, replace the worst individual in the memory bank.
                # Compare the objective function value of each excellent individual with that of each individual in the memory bank. If it is better than the individual in the memory bank, replace it;
                # Repeat this process until all excellent individuals have been compared.
                # The memory bank size is the same as popSize
                for ii, chs_pop in enumerate(pop):
                    if fitness_pop[ii] == memory_CHS_fitness_list[0]:
                        def haiming(MS1, MS2): 
                            return sum(1 for x, y in zip(MS1, MS2) if x != y)
                        if haiming(chs_pop[0], pop[0][0]) == 0:
                            continue
                        else:
                            # Replace the worst individual
                            memory_CHS_list[-1] = pop[ii]
                            memory_CHS_fitness_list[-1] = fitness_pop[ii]
                            # The worst is replaced by the best, and the order is adjusted to the first
                            memory_CHS_list.insert(0, memory_CHS_list.pop())
                            memory_CHS_fitness_list.insert(0, memory_CHS_fitness_list.pop())
                            continue
                    else:
                        for jj, chs_mem in enumerate(memory_CHS_list):
                            if memory_CHS_fitness_list[jj] > fitness_pop[ii]:
                                memory_CHS_list[jj] = pop[ii]
                                memory_CHS_fitness_list[jj] = fitness_pop[ii]
                                break
                
                # Add randomly generated new sequences to improve global search capabilities
                for _ in range(pop_size):
                    MS, OS = self.random_MSOS()
                    CHS = [MS, OS]
                    pop.append(CHS)

            best_fitness = min(fitness_pop)
            mean_fitness = sum(fitness_pop)/len(fitness_pop)
            best_fitness_index = [index for index, value in enumerate(fitness_pop) if value == best_fitness]
            cal_pop_fitness_time = time.time()-cal_fitness_start

            if optimal_fitness == best_fitness:
                optimal_CHS_list += [pop[index] for index in best_fitness_index]
            if len(optimal_CHS_list) > 100000:
                break

            if optimal_fitness > best_fitness:
                optimal_fitness = best_fitness
                optimal_CHS_list = [pop[index] for index in best_fitness_index]
                print("New Optimal Fitness = {} CHS:{}".format(optimal_fitness, optimal_CHS_list[0]))
            best_fitness_list.append(optimal_fitness)
            print("Iteration:{}/{} Optimal:{} Best:{} Mean:{:.2f}".format(i+1, max_iteration, optimal_fitness, best_fitness, mean_fitness))
            
            def remove_duplicates(input_list):
                unique_items = []
                seen_items = set()
                for sublist in input_list:
                    ms_os = tuple(sublist[0]), tuple(sublist[1])
                    if ms_os not in seen_items:
                        unique_items.append(sublist)
                        seen_items.add(ms_os)
                return unique_items
            optimal_CHS_list = remove_duplicates(optimal_CHS_list)

            one_iteration_time = time.time() - iteration_start_time

            # record_of_one_iter: [iteration, optimal_fitness, best_fitness, mean_fitness, pop_num, time, optimal_size]
            record_of_one_iter = [i+1, optimal_fitness, best_fitness, mean_fitness, len(offspring), one_iteration_time, len(optimal_CHS_list)]
            record_list.append(record_of_one_iter)

            iteration_start_time = time.time()

            # Crossover and Mutation
            offspring = []
            for chs, j in zip(pop, range(len(pop))):
                if random.random() < p_crossover:
                    if random.random() < 0.5:
                        tmp = copy.deepcopy(memory_CHS_list)
                    else:
                        tmp = copy.deepcopy(pop)
                        del tmp[j]
                    cross_chs = random.choice(tmp)
                    if random.random() < p_cross_machine:
                        crossover_MS_start = time.time()
                        MS1, MS2 = self.crossover_MS(chs[0], cross_chs[0])
                        offspring.append([MS1, chs[1]])
                        offspring.append([MS2, cross_chs[1]])
                        crossover_MS_time += time.time() - crossover_MS_start
                        # min(fitness_pop)
                    else:
                        crossover_OS_start = time.time()
                        OS1, OS2 = self.crossover_OS(chs[1], cross_chs[1])
                        offspring.append([chs[0], OS1])
                        offspring.append([cross_chs[0], OS2])
                        crossover_OS_time += time.time() - crossover_OS_start
                if random.random() < p_mutation:
                    if random.random() < p_mutation_machine:
                        mutate_MS_start = time.time()
                        new_MS = self.variation_MS(chs[0])
                        offspring.append([new_MS, chs[1]])
                        mutate_MS_time += time.time() - mutate_MS_start
                    else:
                        mutate_OS_start = time.time()
                        # new_OS = self.variation_OS_return_optimal_one(chs[0], chs[1])
                        # offspring.append([chs[0], new_OS])
                        new_OS = self.variation_OS_return_random_multi(chs[0], chs[1])
                        offspring += [[chs[0], OS] for OS in new_OS]
                        mutate_OS_time += time.time() - mutate_OS_start
            print("time one iteration time:{:.3f},cal_pop_fitness_time:{:.3f}/{:.3f}%, select_time:{:.3f}/{:.3f}%, crossover_MS_time:{:.3f}/{:.3f}%, crossover_OS_time:{:.3f}/{:.3f}%, mutate_MS_time:{:.3f}/{:.3f}%, mutate_OS_time:{:.3f}/{:.3f}%".format(
                one_iteration_time, cal_pop_fitness_time, cal_pop_fitness_time/one_iteration_time*100, select_time, select_time/one_iteration_time*100, crossover_MS_time, crossover_MS_time/one_iteration_time*100, crossover_OS_time, crossover_OS_time/one_iteration_time*100, 
                mutate_MS_time, mutate_MS_time/one_iteration_time*100, mutate_OS_time,mutate_OS_time/one_iteration_time*100))

        return optimal_fitness, memory_CHS_list, memory_CHS_fitness_list, record_list

        x = np.linspace(0, max_iteration, max_iteration)
        plt.plot(x, list(fitness.mean for fitness in best_fitness_list),'-k')
        plt.title(
            'the maximum completion time of each iteration for HRC job shop scheduling problem')
        plt.ylabel('Cmax')
        plt.xlabel('Test Num')
        # plt.show()
        print("Final Best Fitness = {} CHS:{}".format(optimal_fitness, optimal_CHS))
        # self.gantt_HRC((self.decoding_MSOS(optimal_CHS[0], optimal_CHS[1]))[0])


    def GA(self, pop_size, p_crossover, p_cross_machine, p_mutation, p_mutation_machine, max_iteration, tSize=3):
        pop = []
        offspring = []
        for _ in range(pop_size):
            MS, OS = self.random_MSOS()
            # CHS:[MS, OS]
            # [[0, 0, 112, 4, 0, 2, 2, 112, 4, 2, 102], [1, 2, 0, 2, 3, 0, 1, 3, 0, 2, 1]]
            CHS = [MS, OS]
            pop.append(CHS)
        return self.GA_initialed_pop(pop, pop_size, p_crossover, p_cross_machine, p_mutation, p_mutation_machine, max_iteration, tSize)