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
