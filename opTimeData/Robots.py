import numpy as np
import sys
import os

sys.path.append('..')  

from fuzzyNumber import SVTNN

# result
# Battery 
# Pick and place battery
time_O11_R1 = 9999
time_O21_R1 = 9999
time_O11_R2 = 9999
time_O21_R2 = 9999
time_O11_R3 = 9999
time_O21_R3 = 9999
# Tighten 4 screws of side
time_O12_R1 = SVTNN(17,50,5,40)
time_O13_R1 = SVTNN(17,50,5,40)
time_O22_R1 = SVTNN(17,50,5,40)
time_O23_R1 = SVTNN(17,50,5,40)
time_O12_R2 = SVTNN(17,50,5,40)
time_O13_R2 = SVTNN(17,50,5,40)
time_O22_R2 = SVTNN(17,50,5,40)
time_O23_R2 = SVTNN(17,50,5,40)
time_O12_R3 = SVTNN(17,50,5,40)
time_O13_R3 = SVTNN(17,50,5,40)
time_O22_R3 = SVTNN(17,50,5,40)
time_O23_R3 = SVTNN(17,50,5,40)

# Controller 
# Pick, prepare and place controller
time_O31_R1 = 9999
time_O41_R1 = 9999
time_O31_R2 = 9999
time_O41_R2 = 9999
time_O31_R3 = 9999
time_O41_R3 = 9999
# Tighten 4 screws - R1
time_O32_R1 = SVTNN(17,50,5,40)
time_O42_R1 = SVTNN(17,50,5,40)
time_O32_R2 = SVTNN(17,50,5,40)
time_O42_R2 = SVTNN(17,50,5,40)
time_O32_R3 = SVTNN(17,50,5,40)
time_O42_R3 = SVTNN(17,50,5,40)


n = 4  # 成功次数
p = 0.8  # 每次成功的概率
g_data = []
for _ in range(100):
    op_time = 0
    failures = np.random.negative_binomial(n, p)
    for _ in range(n+failures):
        op_time += 10
    g_data.append(int(op_time))
    # print(n+failures)
print(g_data)

data = g_data
mean = np.mean(data)
variance = np.var(data)
std = np.std(data)
count_above_mean = np.sum(data > mean)
P = count_above_mean/len(data)
r_std = P*std*2
l_std = (1-P)*std*2

print("SVTNN({},{},{},{})".format(int(l_std), int(mean), int(r_std), min(data)))