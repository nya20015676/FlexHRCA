import numpy as np
import sys
import os

sys.path.append('..')  

from fuzzyNumber import SVTNN

class TimeData:
    time_O11_H1 = SVTNN(5,15,3,10)
    time_O21_H1 = SVTNN(5,15,3,10)
    time_O12_H1 = SVTNN(6,22,5,10)
    time_O13_H1 = SVTNN(6,22,5,10)
    time_O22_H1 = SVTNN(6,22,5,10)
    time_O23_H1 = SVTNN(6,22,5,10)
    time_O31_H1 = SVTNN(6,16,3,10)
    time_O41_H1 = SVTNN(6,16,3,10)
    time_O32_H1 = SVTNN(10,35,8,18)
    time_O42_H1 = SVTNN(10,35,8,18)
    time_O51_H1 = SVTNN(5,104,6,89)

    time_O11_H2 = SVTNN(9,19,6,8)
    time_O21_H2 = SVTNN(9,19,6,8)
    time_O12_H2 = SVTNN(31,86,20,50)
    time_O13_H2 = SVTNN(31,86,20,50)
    time_O22_H2 = SVTNN(31,86,20,50)
    time_O23_H2 = SVTNN(31,86,20,50)
    time_O31_H2 = SVTNN(9,21,6,10)
    time_O41_H2 = SVTNN(9,21,6,10)
    time_O32_H2 = SVTNN(47,143,20,100)
    time_O42_H2 = SVTNN(47,143,20,100)
    time_O51_H2 = SVTNN(7,119,7,89)

    time_O11_H3 = SVTNN(10,21,6,8)
    time_O21_H3 = SVTNN(10,21,6,8)
    time_O12_H3 = SVTNN(52,121,22,60)
    time_O13_H3 = SVTNN(52,121,22,60)
    time_O22_H3 = SVTNN(52,121,22,60)
    time_O23_H3 = SVTNN(52,121,22,60)
    time_O31_H3 = SVTNN(9,22,6,10)
    time_O41_H3 = SVTNN(9,22,6,10)
    time_O32_H3 = SVTNN(70,187,46,130)
    time_O42_H3 = SVTNN(70,187,46,130)
    time_O51_H3 = SVTNN(10,135,6,89)

    time_O11_R1 = 9999
    time_O21_R1 = 9999
    time_O11_R2 = 9999
    time_O21_R2 = 9999
    time_O11_R3 = 9999
    time_O21_R3 = 9999
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
    time_O31_R1 = 9999
    time_O41_R1 = 9999
    time_O31_R2 = 9999
    time_O41_R2 = 9999
    time_O31_R3 = 9999
    time_O41_R3 = 9999
    time_O32_R1 = SVTNN(17,50,5,40)
    time_O42_R1 = SVTNN(17,50,5,40)
    time_O32_R2 = SVTNN(17,50,5,40)
    time_O42_R2 = SVTNN(17,50,5,40)
    time_O32_R3 = SVTNN(17,50,5,40)
    time_O42_R3 = SVTNN(17,50,5,40)

class TimeData_Alpha_Beta:
    def __init__(self, alpha, beta):
        self.time_O11_H1 = SVTNN(5,15,3,10, alpha, beta)
        self.time_O21_H1 = SVTNN(5,15,3,10, alpha, beta)
        self.time_O12_H1 = SVTNN(6,22,5,10, alpha, beta)
        self.time_O13_H1 = SVTNN(6,22,5,10, alpha, beta)
        self.time_O22_H1 = SVTNN(6,22,5,10, alpha, beta)
        self.time_O23_H1 = SVTNN(6,22,5,10, alpha, beta)
        self.time_O31_H1 = SVTNN(6,16,3,10, alpha, beta)
        self.time_O41_H1 = SVTNN(6,16,3,10, alpha, beta)
        self.time_O32_H1 = SVTNN(10,35,8,18, alpha, beta)
        self.time_O42_H1 = SVTNN(10,35,8,18, alpha, beta)
        self.time_O51_H1 = SVTNN(5,104,6,89, alpha, beta)

        self.time_O11_H2 = SVTNN(9,19,6,8, alpha, beta)
        self.time_O21_H2 = SVTNN(9,19,6,8, alpha, beta)
        self.time_O12_H2 = SVTNN(31,86,20,50, alpha, beta)
        self.time_O13_H2 = SVTNN(31,86,20,50, alpha, beta)
        self.time_O22_H2 = SVTNN(31,86,20,50, alpha, beta)
        self.time_O23_H2 = SVTNN(31,86,20,50, alpha, beta)
        self.time_O31_H2 = SVTNN(9,21,6,10, alpha, beta)
        self.time_O41_H2 = SVTNN(9,21,6,10, alpha, beta)
        self.time_O32_H2 = SVTNN(47,143,20,100, alpha, beta)
        self.time_O42_H2 = SVTNN(47,143,20,100, alpha, beta)
        self.time_O51_H2 = SVTNN(7,119,7,89, alpha, beta)

        self.time_O11_H3 = SVTNN(10,21,6,8, alpha, beta)
        self.time_O21_H3 = SVTNN(10,21,6,8, alpha, beta)
        self.time_O12_H3 = SVTNN(52,121,22,60, alpha, beta)
        self.time_O13_H3 = SVTNN(52,121,22,60, alpha, beta)
        self.time_O22_H3 = SVTNN(52,121,22,60, alpha, beta)
        self.time_O23_H3 = SVTNN(52,121,22,60, alpha, beta)
        self.time_O31_H3 = SVTNN(9,22,6,10, alpha, beta)
        self.time_O41_H3 = SVTNN(9,22,6,10, alpha, beta)
        self.time_O32_H3 = SVTNN(70,187,46,130, alpha, beta)
        self.time_O42_H3 = SVTNN(70,187,46,130, alpha, beta)
        self.time_O51_H3 = SVTNN(10,135,6,89, alpha, beta)

        self.time_O11_R1 = 9999
        self.time_O21_R1 = 9999
        self.time_O11_R2 = 9999
        self.time_O21_R2 = 9999
        self.time_O11_R3 = 9999
        self.time_O21_R3 = 9999
        self.time_O12_R1 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O13_R1 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O22_R1 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O23_R1 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O12_R2 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O13_R2 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O22_R2 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O23_R2 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O12_R3 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O13_R3 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O22_R3 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O23_R3 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O31_R1 = 9999
        self.time_O41_R1 = 9999
        self.time_O31_R2 = 9999
        self.time_O41_R2 = 9999
        self.time_O31_R3 = 9999
        self.time_O41_R3 = 9999
        self.time_O32_R1 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O42_R1 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O32_R2 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O42_R2 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O32_R3 = SVTNN(17,50,5,40, alpha, beta)
        self.time_O42_R3 = SVTNN(17,50,5,40, alpha, beta)

SVTN_682_954 = TimeData_Alpha_Beta(0.682, 0.954)
SVTN_682_997 = TimeData_Alpha_Beta(0.682, 0.997)
SVTN_954_997 = TimeData_Alpha_Beta(0.954, 0.997)
