import numpy as np
import sys
import os

sys.path.append('..')  

from fuzzyNumber import SVTNN

# Battery 
# Pick and place battery
data_O11_H3 = [23,16,20,14,22,13,23,10,12,22] # SVTNN(10,21,6,8)
data_O21_H3 = [23,16,20,14,22,13,23,10,12,22] # SVTNN(10,21,6,8)
# Tighten 4 screws of side
data_O12_H3 = [113, 114, 95, 92, 160, 122, 211, 121, 69, 115] # SVTNN(52,121,22,60)
data_O13_H3 = [113, 114, 95, 92, 160, 122, 211, 121, 69, 115] # SVTNN(52,121,22,60)
data_O22_H3 = [113, 114, 95, 92, 160, 122, 211, 121, 69, 115] # SVTNN(52,121,22,60)
data_O23_H3 = [113, 114, 95, 92, 160, 122, 211, 121, 69, 115] # SVTNN(52,121,22,60)

# Controller 
# Pick, prepare and place controller
data_O31_H3 = [12, 16, 19, 25, 22, 20, 14, 25, 26, 14] # SVTNN(9,22,6,10)
data_O41_H3 = [12, 16, 19, 25, 22, 20, 14, 25, 26, 14] # SVTNN(9,22,6,10)
# Tighten 4 screws - H3
data_O32_H3 = [201, 349, 199, 170, 153, 164, 198, 163, 138, 136] # SVTNN(70,187,46,130)
data_O42_H3 = [201, 349, 199, 170, 153, 164, 198, 163, 138, 136] # SVTNN(70,187,46,130)

# Install components and connect cables for controllers
data_O51_H3 = [128, 135, 137, 135, 128, 135, 122, 134, 140, 133] # SVTNN(10,135,6,89)

# result
# Battery 
# Pick and place battery
time_O11_H3 = SVTNN(10,21,6,8)
time_O21_H3 = SVTNN(10,21,6,8)
# Tighten 4 screws of side
time_O12_H3 = SVTNN(52,121,22,60)
time_O13_H3 = SVTNN(52,121,22,60)
time_O22_H3 = SVTNN(52,121,22,60)
time_O23_H3 = SVTNN(52,121,22,60)

# Controller 
# Pick, prepare and place controller
time_O31_H3 = SVTNN(9,22,6,10)
time_O41_H3 = SVTNN(9,22,6,10)
# Tighten 4 screws - H3
time_O32_H3 = SVTNN(70,187,46,130)
time_O42_H3 = SVTNN(70,187,46,130)

# Install components and connect cables for controllers
time_O51_H3 = SVTNN(10,135,6,89)
