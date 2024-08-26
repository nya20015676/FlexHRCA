import numpy as np
import sys
import os

sys.path.append('..')  

from fuzzyNumber import Triangular

class TimeData:
    time_O11_H1 = Triangular(5,15,3,10)
    time_O21_H1 = Triangular(5,15,3,10)
    time_O12_H1 = Triangular(6,22,5,10)
    time_O13_H1 = Triangular(6,22,5,10)
    time_O22_H1 = Triangular(6,22,5,10)
    time_O23_H1 = Triangular(6,22,5,10)
    time_O31_H1 = Triangular(6,16,3,10)
    time_O41_H1 = Triangular(6,16,3,10)
    time_O32_H1 = Triangular(10,35,8,18)
    time_O42_H1 = Triangular(10,35,8,18)
    time_O51_H1 = Triangular(5,104,6,89)

    time_O11_H2 = Triangular(9,19,6,8)
    time_O21_H2 = Triangular(9,19,6,8)
    time_O12_H2 = Triangular(31,86,20,50)
    time_O13_H2 = Triangular(31,86,20,50)
    time_O22_H2 = Triangular(31,86,20,50)
    time_O23_H2 = Triangular(31,86,20,50)
    time_O31_H2 = Triangular(9,21,6,10)
    time_O41_H2 = Triangular(9,21,6,10)
    time_O32_H2 = Triangular(47,143,20,100)
    time_O42_H2 = Triangular(47,143,20,100)
    time_O51_H2 = Triangular(7,119,7,89)

    time_O11_H3 = Triangular(10,21,6,8)
    time_O21_H3 = Triangular(10,21,6,8)
    time_O12_H3 = Triangular(52,121,22,60)
    time_O13_H3 = Triangular(52,121,22,60)
    time_O22_H3 = Triangular(52,121,22,60)
    time_O23_H3 = Triangular(52,121,22,60)
    time_O31_H3 = Triangular(9,22,6,10)
    time_O41_H3 = Triangular(9,22,6,10)
    time_O32_H3 = Triangular(70,187,46,130)
    time_O42_H3 = Triangular(70,187,46,130)
    time_O51_H3 = Triangular(10,135,6,89)

    time_O11_R1 = 9999
    time_O21_R1 = 9999
    time_O11_R2 = 9999
    time_O21_R2 = 9999
    time_O11_R3 = 9999
    time_O21_R3 = 9999
    time_O12_R1 = Triangular(17,50,5,40)
    time_O13_R1 = Triangular(17,50,5,40)
    time_O22_R1 = Triangular(17,50,5,40)
    time_O23_R1 = Triangular(17,50,5,40)
    time_O12_R2 = Triangular(17,50,5,40)
    time_O13_R2 = Triangular(17,50,5,40)
    time_O22_R2 = Triangular(17,50,5,40)
    time_O23_R2 = Triangular(17,50,5,40)
    time_O12_R3 = Triangular(17,50,5,40)
    time_O13_R3 = Triangular(17,50,5,40)
    time_O22_R3 = Triangular(17,50,5,40)
    time_O23_R3 = Triangular(17,50,5,40)
    time_O31_R1 = 9999
    time_O41_R1 = 9999
    time_O31_R2 = 9999
    time_O41_R2 = 9999
    time_O31_R3 = 9999
    time_O41_R3 = 9999
    time_O32_R1 = Triangular(17,50,5,40)
    time_O42_R1 = Triangular(17,50,5,40)
    time_O32_R2 = Triangular(17,50,5,40)
    time_O42_R2 = Triangular(17,50,5,40)
    time_O32_R3 = Triangular(17,50,5,40)
    time_O42_R3 = Triangular(17,50,5,40)

