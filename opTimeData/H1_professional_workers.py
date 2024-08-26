import numpy as np
import sys
import os

sys.path.append('..')  

from fuzzyNumber import SVTNN

# result
# Battery 
# Pick and place battery
time_O11_H1 = SVTNN(5,15,3,10)
time_O21_H1 = SVTNN(5,15,3,10)
# Tighten 4 screws of side
time_O12_H1 = SVTNN(6,22,5,10)
time_O13_H1 = SVTNN(6,22,5,10)
time_O22_H1 = SVTNN(6,22,5,10)
time_O23_H1 = SVTNN(6,22,5,10)

# Controller 
# Pick, prepare and place controller
time_O31_H1 = SVTNN(6,16,3,10)
time_O41_H1 = SVTNN(6,16,3,10)
# Tighten 4 screws - H1
time_O32_H1 = SVTNN(10,35,8,18)
time_O42_H1 = SVTNN(10,35,8,18)

# Install components and connect cables for controllers
time_O51_H1 = SVTNN(5,104,6,89)
