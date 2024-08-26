import sys

sys.path.append('..')  
sys.path.append('../..')  
sys.path.append('../../..')  
sys.path.append('../../../..')  
sys.path.append('../../../../HnRnTest')  
sys.path.append('../../../../opTimeData')  
from hrcStation import Human, Robot, Productt, HrcStation
from fuzzyNumber import Triangular, SVTNN
from scipy.stats import norm, nbinom
from openpyxl import Workbook
import pickle
import os
import send2trash
import itertools
import copy
from time_data import TimeData,TimeData,SVTN_682_997,SVTN_954_997
from Time import TIME_TABLE
import random
import numpy as np

for lst in TIME_TABLE.Time_H4R1:
      for i in range(len(lst)):
          if lst[i] != 9999:
              lst[i].sampling()
for lst in TIME_TABLE.Time_H4R2:
      for i in range(len(lst)):
          if lst[i] != 9999:
              lst[i].sampling()
for lst in TIME_TABLE.Time_H4R3:
      for i in range(len(lst)):
          if lst[i] != 9999:
              lst[i].sampling()
for lst in TIME_TABLE.Time_H4R4:
      for i in range(len(lst)):
          if lst[i] != 9999:
              lst[i].sampling()
for lst in TIME_TABLE.Time_H4R5:
      for i in range(len(lst)):
          if lst[i] != 9999:
              lst[i].sampling()

def test_one_CHS_one_cycle(CHS, n_robots):
    def randomTime_SVTNN2static(Time):
        new_Time = copy.deepcopy(Time)
        for lst in new_Time:
            for i in range(len(lst)):
                if lst[i] != 9999:
                    lst[i] = lst[i].random()
        return new_Time
   
    human1 = Human("human1", capability = 3)
    human2 = Human("human2", capability = 6)
    human3 = Human("human3", capability = 6)
    human4 = Human("human4", capability = 6)
    human5 = Human("human5", capability = 6)
    robot1 = Robot("robot1", capability = 3)
    robot2 = Robot("robot2", capability = 5)
    robot3 = Robot("robot3", capability = 8)
    robot4 = Robot("robot4", capability = 8)
    robot5 = Robot("robot5", capability = 8)
    robots_list = [[robot1], [robot1, robot2], [robot1, robot2, robot3], [robot1, robot2, robot3, robot4], [robot1, robot2, robot3, robot4, robot5]]
    product1 = Productt("Battery pack")
    product2 = Productt("Battery pack")
    product3 = Productt("Battery pack")
    #Product
    n_job_op = {0:3, 1:3, 2:2, 3:2, 4:1}
    after_require = [ # 0~2 Battery1 installation
                        [], [0], [0],
                    # 3~5 Battery2 installation
                        [], [3], [3],
                    # 6~7 Controller1 installation
                        [], [6], 
                    # 8~9 Controller2 installation
                        [], [8],  ]
    after_require.append(list(range(10)))
    product1.set_jobs(n_job_op, after_require)
    product2.set_jobs(n_job_op, after_require)
    product3.set_jobs(n_job_op, after_require)
    station_static = HrcStation()
    if n_robots == 1:
        station_static.set_operator_product_Time([human1, human2, human3, human4], robots_list[n_robots-1], [product1, product2, product3], [randomTime_SVTNN2static(TIME_TABLE.Time_H4R1), randomTime_SVTNN2static(TIME_TABLE.Time_H4R1), randomTime_SVTNN2static(TIME_TABLE.Time_H4R1)])
    if n_robots == 2:
        station_static.set_operator_product_Time([human1, human2, human3, human4], robots_list[n_robots-1], [product1, product2, product3], [randomTime_SVTNN2static(TIME_TABLE.Time_H4R2), randomTime_SVTNN2static(TIME_TABLE.Time_H4R2), randomTime_SVTNN2static(TIME_TABLE.Time_H4R2)])
    if n_robots == 3:
        station_static.set_operator_product_Time([human1, human2, human3, human4], robots_list[n_robots-1], [product1, product2, product3], [randomTime_SVTNN2static(TIME_TABLE.Time_H4R3), randomTime_SVTNN2static(TIME_TABLE.Time_H4R3), randomTime_SVTNN2static(TIME_TABLE.Time_H4R3)])
    if n_robots == 4:
        station_static.set_operator_product_Time([human1, human2, human3, human4], robots_list[n_robots-1], [product1, product2, product3], [randomTime_SVTNN2static(TIME_TABLE.Time_H4R4), randomTime_SVTNN2static(TIME_TABLE.Time_H4R4), randomTime_SVTNN2static(TIME_TABLE.Time_H4R4)])
    if n_robots == 5:
        station_static.set_operator_product_Time([human1, human2, human3, human4], robots_list[n_robots-1], [product1, product2, product3], [randomTime_SVTNN2static(TIME_TABLE.Time_H4R5), randomTime_SVTNN2static(TIME_TABLE.Time_H4R5), randomTime_SVTNN2static(TIME_TABLE.Time_H4R5)])
    return station_static.calculate_fitness(CHS[0], CHS[1])

def test_CHSs(filename, n_robots):
    with open(filename, 'rb') as file:
        
        CHS_list = pickle.load(file)
    All = []
    CHS_fitness = []
    CHS_fitness_range = []
    CHS_fitness_std = []
    CHS_fitness_max = []
    CHS_fitness_min = []
    for i, CHS in enumerate(CHS_list):
        total = []
        for _ in range(20):
            fitness = test_one_CHS_one_cycle(CHS, n_robots)
            total.append(fitness)
            All.append(fitness)
        CHS_fitness.append(np.mean(np.array(total)))
        CHS_fitness_std.append(np.sqrt(np.var(np.array(total))))
        CHS_fitness_range.append(max(total)-min(total))
        CHS_fitness_max.append(max(total))
        CHS_fitness_min.append(min(total))
    wb = Workbook()
    ws = wb.active
    for row in All:
        ws.append([row])
    excel_name = os.path.dirname(filename)+'/'+os.path.splitext(os.path.basename(filename))[0]+"-testdata.xlsx"
    if os.path.exists(excel_name):
        send2trash.send2trash(excel_name)  
    wb.save(excel_name)
    # mean, std, range, max, min
    return np.mean(np.array(CHS_fitness)), np.mean(np.array(CHS_fitness_std)), np.mean(np.array(CHS_fitness_range)), np.mean(np.array(CHS_fitness_max)), np.mean(np.array(CHS_fitness_min))

def test_CHS(filename, n_robots):
    with open(filename, 'rb') as file:
        
        CHS_list = pickle.load(file)

    CHS = CHS_list[0]
    total = []
    for _ in range(100):
        total.append(test_one_CHS_one_cycle(CHS, n_robots))
    
    return np.mean(np.array(total)), np.sqrt(np.var(np.array(total)))

def find_bestCHS_pickle(filename):
    with open(filename, 'rb') as file:
        
        CHS_list = pickle.load(file)
    CHS_fitness = []
    for i, CHS in enumerate(CHS_list):
        total = 0
        for _ in range(10):
            total += test_one_CHS_one_cycle(CHS)
        CHS_fitness.append(total/10)
    return min(CHS_fitness), CHS_list[CHS_fitness.index(min(CHS_fitness))]

def find_worstCHS_pickle(filename):
    with open(filename, 'rb') as file:
        
        CHS_list = pickle.load(file)
    CHS_fitness = []
    for i, CHS in enumerate(CHS_list):
        total = 0
        for _ in range(10):
            total += test_one_CHS_one_cycle(CHS)
        CHS_fitness.append(total/10)
    return max(CHS_fitness), CHS_list[CHS_fitness.index(min(CHS_fitness))]

path_list = ["/home/amtc/Desktop/optimal/comparison/CSP/H4/H4R2/",
             
             ]

for i, path in enumerate(path_list):
    output = ""
    for file_name in os.listdir(path):
        if not file_name.endswith(".pickle"):
            continue
        outcome_mean, outcome_std, outcome_range, outcome_max, outcome_min = test_CHSs(path+file_name, i+2)
        # outcome_mean, outcome_std = test_CHS(path+min_file, i+1)
        output += file_name[0:2] + " "
        output += "{:.2f}".format(outcome_mean) + " "
        output += "{:.2f}".format(outcome_std) + " "
        output += "{:.2f}".format(outcome_range) + " "
        output += "{:.2f}".format(outcome_max) + " "
        output += "{:.2f}".format(outcome_min) + " "
        output += "\n"
        print(output)
    # with open(path + "result.txt", "w") as file:
    #         file.write(output)