import numpy as np
from fuzzyNumber import SVTNN

# Battery 
# Pick and place battery
data_O11_H2 = [33,23,25,28,15,18,16, 8,11,13] # SVTNN(9,19,6,8)
data_O21_H2 = [33,23,25,28,15,18,16, 8,11,13] # SVTNN(9,19,6,8)
# Tighten 4 screws of side
data_O12_H2 = [70,80,75,77,139,61,57,131,91,88] # SVTNN(31,86,20,50)
data_O13_H2 = [70,80,75,77,139,61,57,131,91,88] # SVTNN(31,86,20,50)
data_O22_H2 = [70,80,75,77,139,61,57,131,91,88] # SVTNN(31,86,20,50)
data_O23_H2 = [70,80,75,77,139,61,57,131,91,88] # SVTNN(31,86,20,50)

# Controller 
# Pick, prepare and place controller
data_O31_H2 = [36,18,26,28,31,16,11,14,21,18] # SVTNN(9,21,6,10)
data_O41_H2 = [36,18,26,28,31,16,11,14,21,18] # SVTNN(9,21,6,10)
# Tighten 4 screws - H2
data_O32_H2 = [103,188,142,103,132,134,184,201,114,129] # SVTNN(47,143,20,100)
data_O42_H2 = [103,188,142,103,132,134,184,201,114,129] # SVTNN(47,143,20,100)

# Install components and connect cables for controllers
data_O51_H2 = [89+40,89+35,89+42,89+28,89+37,89+20,89+23,89+20,89+33,89+26] # SVTNN(7,119,7,89)

# result
# Battery 
# Pick and place battery
time_O11_H2 = SVTNN(9,19,6,8)
time_O21_H2 = SVTNN(9,19,6,8)
# Tighten 4 screws of side
time_O12_H2 = SVTNN(31,86,20,50)
time_O13_H2 = SVTNN(31,86,20,50)
time_O22_H2 = SVTNN(31,86,20,50)
time_O23_H2 = SVTNN(31,86,20,50)

# Controller 
# Pick, prepare and place controller
time_O31_H2 = SVTNN(9,21,6,10)
time_O41_H2 = SVTNN(9,21,6,10)
# Tighten 4 screws - H2
time_O32_H2 = SVTNN(47,143,20,100)
time_O42_H2 = SVTNN(47,143,20,100)

# Install components and connect cables for controllers
time_O51_H2 = SVTNN(7,119,7,89)
