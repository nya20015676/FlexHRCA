import sys
import copy
import pickle
import os

sys.path.append('..') 
sys.path.append('../..') 
from time_data import TimeData
from fuzzyNumber import FuzzyNumber

instance_types = ["H1R1","H2R2","H2R4","H3R1","H3R3","H4R1","H4R2","H5R1", "H5R2"]

use_case_H1R1 = [
    [15, 3, 1],
    [3, 1, 1,TimeData.time_O11_H1, 2, 1,TimeData.time_O12_H1,2,TimeData.time_O12_R1, 2, 1,TimeData.time_O13_H1,2,TimeData.time_O13_R1],
    [3, 1, 1,TimeData.time_O21_H1, 2, 1,TimeData.time_O22_H1,2,TimeData.time_O22_R1, 2, 1,TimeData.time_O23_H1,2,TimeData.time_O23_R1],
    [2, 1, 1,TimeData.time_O31_H1, 2, 1,TimeData.time_O32_H1,2,TimeData.time_O32_R1],
    [2, 1, 1,TimeData.time_O41_H1, 2, 1,TimeData.time_O42_H1,2,TimeData.time_O42_R1],
    [1, 1, 3,TimeData.time_O51_H1],
    [3, 1, 1,TimeData.time_O11_H1, 2, 1,TimeData.time_O12_H1,2,TimeData.time_O12_R1, 2, 1,TimeData.time_O13_H1,2,TimeData.time_O13_R1],
    [3, 1, 1,TimeData.time_O21_H1, 2, 1,TimeData.time_O22_H1,2,TimeData.time_O22_R1, 2, 1,TimeData.time_O23_H1,2,TimeData.time_O23_R1],
    [2, 1, 1,TimeData.time_O31_H1, 2, 1,TimeData.time_O32_H1,2,TimeData.time_O32_R1],
    [2, 1, 1,TimeData.time_O41_H1, 2, 1,TimeData.time_O42_H1,2,TimeData.time_O42_R1],
    [1, 1, 3,TimeData.time_O51_H1],
    [3, 1, 1,TimeData.time_O11_H1, 2, 1,TimeData.time_O12_H1,2,TimeData.time_O12_R1, 2, 1,TimeData.time_O13_H1,2,TimeData.time_O13_R1],
    [3, 1, 1,TimeData.time_O21_H1, 2, 1,TimeData.time_O22_H1,2,TimeData.time_O22_R1, 2, 1,TimeData.time_O23_H1,2,TimeData.time_O23_R1],
    [2, 1, 1,TimeData.time_O31_H1, 2, 1,TimeData.time_O32_H1,2,TimeData.time_O32_R1],
    [2, 1, 1,TimeData.time_O41_H1, 2, 1,TimeData.time_O42_H1,2,TimeData.time_O42_R1],
    [1, 1, 3,TimeData.time_O51_H1],
]

use_case_H2R2 = [
    [15, 8, 2],
    [3, 2, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2, 4, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_R1,4,TimeData.time_O12_R2, 4, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_R1,4,TimeData.time_O13_R2],
    [3, 2, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2, 4, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_R1,4,TimeData.time_O22_R2, 4, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_R1,4,TimeData.time_O23_R2],
    [2, 2, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2, 4, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_R1,4,TimeData.time_O32_R2],
    [2, 2, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2, 4, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_R1,4,TimeData.time_O42_R2],
    [1, 2, 5,TimeData.time_O51_H1,7,TimeData.time_O51_H2],
    [3, 2, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2, 4, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_R1,4,TimeData.time_O12_R2, 4, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_R1,4,TimeData.time_O13_R2],
    [3, 2, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2, 4, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_R1,4,TimeData.time_O22_R2, 4, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_R1,4,TimeData.time_O23_R2],
    [2, 2, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2, 4, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_R1,4,TimeData.time_O32_R2],
    [2, 2, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2, 4, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_R1,4,TimeData.time_O42_R2],
    [1, 2, 5,TimeData.time_O51_H1,7,TimeData.time_O51_H2],
    [3, 2, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2, 4, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_R1,4,TimeData.time_O12_R2, 4, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_R1,4,TimeData.time_O13_R2],
    [3, 2, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2, 4, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_R1,4,TimeData.time_O22_R2, 4, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_R1,4,TimeData.time_O23_R2],
    [2, 2, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2, 4, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_R1,4,TimeData.time_O32_R2],
    [2, 2, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2, 4, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_R1,4,TimeData.time_O42_R2],
    [1, 2, 5,TimeData.time_O51_H1,7,TimeData.time_O51_H2],
]

use_case_H2R4 = [
    [15, 14, 2],
    [3, 2, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2, 6, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_R1,4,TimeData.time_O12_R2,5,TimeData.time_O12_R3,6,TimeData.time_O12_R3, 6, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_R1,4,TimeData.time_O13_R2,5,TimeData.time_O13_R3,6,TimeData.time_O13_R3],
    [3, 2, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2, 6, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_R1,4,TimeData.time_O22_R2,5,TimeData.time_O22_R3,6,TimeData.time_O22_R3, 6, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_R1,4,TimeData.time_O23_R2,5,TimeData.time_O23_R3,6,TimeData.time_O23_R3],
    [2, 2, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2, 6, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_R1,4,TimeData.time_O32_R2,5,TimeData.time_O32_R3,6,TimeData.time_O32_R3],
    [2, 2, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2, 6, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_R1,4,TimeData.time_O42_R2,5,TimeData.time_O42_R3,6,TimeData.time_O42_R3],
    [1, 2, 7,TimeData.time_O51_H1,11,TimeData.time_O51_H2],
    [3, 2, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2, 6, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_R1,4,TimeData.time_O12_R2,5,TimeData.time_O12_R3,6,TimeData.time_O12_R3, 6, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_R1,4,TimeData.time_O13_R2,5,TimeData.time_O13_R3,6,TimeData.time_O13_R3],
    [3, 2, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2, 6, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_R1,4,TimeData.time_O22_R2,5,TimeData.time_O22_R3,6,TimeData.time_O22_R3, 6, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_R1,4,TimeData.time_O23_R2,5,TimeData.time_O23_R3,6,TimeData.time_O23_R3],
    [2, 2, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2, 6, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_R1,4,TimeData.time_O32_R2,5,TimeData.time_O32_R3,6,TimeData.time_O32_R3],
    [2, 2, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2, 6, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_R1,4,TimeData.time_O42_R2,5,TimeData.time_O42_R3,6,TimeData.time_O42_R3],
    [1, 2, 7,TimeData.time_O51_H1,11,TimeData.time_O51_H2],
    [3, 2, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2, 6, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_R1,4,TimeData.time_O12_R2,5,TimeData.time_O12_R3,6,TimeData.time_O12_R3, 6, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_R1,4,TimeData.time_O13_R2,5,TimeData.time_O13_R3,6,TimeData.time_O13_R3],
    [3, 2, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2, 6, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_R1,4,TimeData.time_O22_R2,5,TimeData.time_O22_R3,6,TimeData.time_O22_R3, 6, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_R1,4,TimeData.time_O23_R2,5,TimeData.time_O23_R3,6,TimeData.time_O23_R3],
    [2, 2, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2, 6, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_R1,4,TimeData.time_O32_R2,5,TimeData.time_O32_R3,6,TimeData.time_O32_R3],
    [2, 2, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2, 6, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_R1,4,TimeData.time_O42_R2,5,TimeData.time_O42_R3,6,TimeData.time_O42_R3],
    [1, 2, 7,TimeData.time_O51_H1,11,TimeData.time_O51_H2],
]

use_case_H3R1 = [
    [15, 7, 2],
    [3, 3, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3, 4, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_R1, 4, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_R1],
    [3, 3, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3, 4, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_R1, 4, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_R1],
    [2, 3, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3, 4, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_R1],
    [2, 3, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3, 4, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_R1],
    [1, 3, 5,TimeData.time_O51_H1,6,TimeData.time_O51_H2,7,TimeData.time_O51_H3],
    [3, 3, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3, 4, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_R1, 4, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_R1],
    [3, 3, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3, 4, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_R1, 4, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_R1],
    [2, 3, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3, 4, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_R1],
    [2, 3, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3, 4, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_R1],
    [1, 3, 5,TimeData.time_O51_H1,6,TimeData.time_O51_H2,7,TimeData.time_O51_H3],
    [3, 3, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3, 4, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_R1, 4, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_R1],
    [3, 3, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3, 4, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_R1, 4, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_R1],
    [2, 3, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3, 4, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_R1],
    [2, 3, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3, 4, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_R1],
    [1, 3, 5,TimeData.time_O51_H1,6,TimeData.time_O51_H2,7,TimeData.time_O51_H3],
]

use_case_H3R3 =[
    [15, 15, 3],
    [3, 3, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3, 6, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_R1,5,TimeData.time_O12_R2,6,TimeData.time_O12_R3, 6, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_R1,5,TimeData.time_O13_R2,6,TimeData.time_O13_R3],
    [3, 3, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3, 6, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_R1,5,TimeData.time_O22_R2,6,TimeData.time_O22_R3, 6, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_R1,5,TimeData.time_O23_R2,6,TimeData.time_O23_R3],
    [2, 3, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3, 6, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_R1,5,TimeData.time_O32_R2,6,TimeData.time_O32_R3],
    [2, 3, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3, 6, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_R1,5,TimeData.time_O42_R2,6,TimeData.time_O42_R3],
    [1, 3, 7,TimeData.time_O51_H1,10,TimeData.time_O51_H2,13,TimeData.time_O51_H3],
    [3, 3, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3, 6, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_R1,5,TimeData.time_O12_R2,6,TimeData.time_O12_R3, 6, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_R1,5,TimeData.time_O13_R2,6,TimeData.time_O13_R3],
    [3, 3, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3, 6, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_R1,5,TimeData.time_O22_R2,6,TimeData.time_O22_R3, 6, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_R1,5,TimeData.time_O23_R2,6,TimeData.time_O23_R3],
    [2, 3, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3, 6, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_R1,5,TimeData.time_O32_R2,6,TimeData.time_O32_R3],
    [2, 3, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3, 6, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_R1,5,TimeData.time_O42_R2,6,TimeData.time_O42_R3],
    [1, 3, 7,TimeData.time_O51_H1,10,TimeData.time_O51_H2,13,TimeData.time_O51_H3],
    [3, 3, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3, 6, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_R1,5,TimeData.time_O12_R2,6,TimeData.time_O12_R3, 6, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_R1,5,TimeData.time_O13_R2,6,TimeData.time_O13_R3],
    [3, 3, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3, 6, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_R1,5,TimeData.time_O22_R2,6,TimeData.time_O22_R3, 6, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_R1,5,TimeData.time_O23_R2,6,TimeData.time_O23_R3],
    [2, 3, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3, 6, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_R1,5,TimeData.time_O32_R2,6,TimeData.time_O32_R3],
    [2, 3, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3, 6, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_R1,5,TimeData.time_O42_R2,6,TimeData.time_O42_R3],
    [1, 3, 7,TimeData.time_O51_H1,10,TimeData.time_O51_H2,13,TimeData.time_O51_H3],
]

use_case_H4R1 = [
    [15, 9, 3],
    [3, 4, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3,4,TimeData.time_O11_H3, 5, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_H3,5,TimeData.time_O12_R1, 5, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_H3,5,TimeData.time_O13_R1],
    [3, 4, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3,4,TimeData.time_O21_H3, 5, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_H3,5,TimeData.time_O22_R1, 5, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_H3,5,TimeData.time_O23_R1],
    [2, 4, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3,4,TimeData.time_O31_H3, 5, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_H3,5,TimeData.time_O32_R1],
    [2, 4, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3,4,TimeData.time_O41_H3, 5, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_H3,5,TimeData.time_O42_R1],
    [1, 4, 6,TimeData.time_O51_H1,7,TimeData.time_O51_H2,8,TimeData.time_O51_H3,9,TimeData.time_O51_H3],
    [3, 4, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3,4,TimeData.time_O11_H3, 5, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_H3,5,TimeData.time_O12_R1, 5, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_H3,5,TimeData.time_O13_R1],
    [3, 4, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3,4,TimeData.time_O21_H3, 5, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_H3,5,TimeData.time_O22_R1, 5, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_H3,5,TimeData.time_O23_R1],
    [2, 4, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3,4,TimeData.time_O31_H3, 5, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_H3,5,TimeData.time_O32_R1],
    [2, 4, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3,4,TimeData.time_O41_H3, 5, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_H3,5,TimeData.time_O42_R1],
    [1, 4, 6,TimeData.time_O51_H1,7,TimeData.time_O51_H2,8,TimeData.time_O51_H3,9,TimeData.time_O51_H3],
    [3, 4, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3,4,TimeData.time_O11_H3, 5, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_H3,5,TimeData.time_O12_R1, 5, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_H3,5,TimeData.time_O13_R1],
    [3, 4, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3,4,TimeData.time_O21_H3, 5, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_H3,5,TimeData.time_O22_R1, 5, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_H3,5,TimeData.time_O23_R1],
    [2, 4, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3,4,TimeData.time_O31_H3, 5, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_H3,5,TimeData.time_O32_R1],
    [2, 4, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3,4,TimeData.time_O41_H3, 5, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_H3,5,TimeData.time_O42_R1],
    [1, 4, 6,TimeData.time_O51_H1,7,TimeData.time_O51_H2,8,TimeData.time_O51_H3,9,TimeData.time_O51_H3],
]

use_case_H4R2 = [
    [15, 14, 3],
    [3, 4, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3,4,TimeData.time_O11_H3, 6, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_H3,5,TimeData.time_O12_R1,6,TimeData.time_O12_R2, 6, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_H3,5,TimeData.time_O13_R1,6,TimeData.time_O13_R2],
    [3, 4, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3,4,TimeData.time_O21_H3, 6, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_H3,5,TimeData.time_O22_R1,6,TimeData.time_O22_R2, 6, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_H3,5,TimeData.time_O23_R1,6,TimeData.time_O23_R2],
    [2, 4, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3,4,TimeData.time_O31_H3, 6, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_H3,5,TimeData.time_O32_R1,6,TimeData.time_O32_R2],
    [2, 4, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3,4,TimeData.time_O41_H3, 5, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_H3,5,TimeData.time_O42_R1,6,TimeData.time_O42_R2],
    [1, 4, 7,TimeData.time_O51_H1,9,TimeData.time_O51_H2,11,TimeData.time_O51_H3,13,TimeData.time_O51_H3],
    [3, 4, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3,4,TimeData.time_O11_H3, 6, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_H3,5,TimeData.time_O12_R1,6,TimeData.time_O12_R2, 6, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_H3,5,TimeData.time_O13_R1,6,TimeData.time_O13_R2],
    [3, 4, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3,4,TimeData.time_O21_H3, 6, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_H3,5,TimeData.time_O22_R1,6,TimeData.time_O22_R2, 6, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_H3,5,TimeData.time_O23_R1,6,TimeData.time_O23_R2],
    [2, 4, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3,4,TimeData.time_O31_H3, 6, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_H3,5,TimeData.time_O32_R1,6,TimeData.time_O32_R2],
    [2, 4, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3,4,TimeData.time_O41_H3, 5, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_H3,5,TimeData.time_O42_R1,6,TimeData.time_O42_R2],
    [1, 4, 7,TimeData.time_O51_H1,9,TimeData.time_O51_H2,11,TimeData.time_O51_H3,13,TimeData.time_O51_H3],
    [3, 4, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3,4,TimeData.time_O11_H3, 6, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_H3,5,TimeData.time_O12_R1,6,TimeData.time_O12_R2, 6, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_H3,5,TimeData.time_O13_R1,6,TimeData.time_O13_R2],
    [3, 4, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3,4,TimeData.time_O21_H3, 6, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_H3,5,TimeData.time_O22_R1,6,TimeData.time_O22_R2, 6, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_H3,5,TimeData.time_O23_R1,6,TimeData.time_O23_R2],
    [2, 4, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3,4,TimeData.time_O31_H3, 6, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_H3,5,TimeData.time_O32_R1,6,TimeData.time_O32_R2],
    [2, 4, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3,4,TimeData.time_O41_H3, 5, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_H3,5,TimeData.time_O42_R1,6,TimeData.time_O42_R2],
    [1, 4, 7,TimeData.time_O51_H1,9,TimeData.time_O51_H2,11,TimeData.time_O51_H3,13,TimeData.time_O51_H3],
]

use_case_H5R1 = [
    [15, 11, 4],
    [3, 5, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3,4,TimeData.time_O11_H3,5,TimeData.time_O11_H3, 6, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_H3,5,TimeData.time_O12_H3,6,TimeData.time_O12_R1, 6, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_H3,5,TimeData.time_O13_H3,6,TimeData.time_O13_R1],
    [3, 5, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3,4,TimeData.time_O21_H3,5,TimeData.time_O21_H3, 6, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_H3,5,TimeData.time_O22_H3,6,TimeData.time_O22_R1, 6, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_H3,5,TimeData.time_O23_H3,6,TimeData.time_O23_R1],
    [2, 5, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3,4,TimeData.time_O31_H3,5,TimeData.time_O31_H3, 6, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_H3,5,TimeData.time_O32_H3,6,TimeData.time_O32_R1],
    [2, 5, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3,4,TimeData.time_O41_H3,5,TimeData.time_O41_H3, 6, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_H3,5,TimeData.time_O42_H3,6,TimeData.time_O42_R1],
    [1, 5, 7,TimeData.time_O51_H1,8,TimeData.time_O51_H2,9,TimeData.time_O51_H3,10,TimeData.time_O51_H3,11,TimeData.time_O51_H3],
    [3, 5, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3,4,TimeData.time_O11_H3,5,TimeData.time_O11_H3, 6, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_H3,5,TimeData.time_O12_H3,6,TimeData.time_O12_R1, 6, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_H3,5,TimeData.time_O13_H3,6,TimeData.time_O13_R1],
    [3, 5, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3,4,TimeData.time_O21_H3,5,TimeData.time_O21_H3, 6, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_H3,5,TimeData.time_O22_H3,6,TimeData.time_O22_R1, 6, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_H3,5,TimeData.time_O23_H3,6,TimeData.time_O23_R1],
    [2, 5, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3,4,TimeData.time_O31_H3,5,TimeData.time_O31_H3, 6, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_H3,5,TimeData.time_O32_H3,6,TimeData.time_O32_R1],
    [2, 5, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3,4,TimeData.time_O41_H3,5,TimeData.time_O41_H3, 6, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_H3,5,TimeData.time_O42_H3,6,TimeData.time_O42_R1],
    [1, 5, 7,TimeData.time_O51_H1,8,TimeData.time_O51_H2,9,TimeData.time_O51_H3,10,TimeData.time_O51_H3,11,TimeData.time_O51_H3],
    [3, 5, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3,4,TimeData.time_O11_H3,5,TimeData.time_O11_H3, 6, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_H3,5,TimeData.time_O12_H3,6,TimeData.time_O12_R1, 6, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_H3,5,TimeData.time_O13_H3,6,TimeData.time_O13_R1],
    [3, 5, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3,4,TimeData.time_O21_H3,5,TimeData.time_O21_H3, 6, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_H3,5,TimeData.time_O22_H3,6,TimeData.time_O22_R1, 6, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_H3,5,TimeData.time_O23_H3,6,TimeData.time_O23_R1],
    [2, 5, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3,4,TimeData.time_O31_H3,5,TimeData.time_O31_H3, 6, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_H3,5,TimeData.time_O32_H3,6,TimeData.time_O32_R1],
    [2, 5, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3,4,TimeData.time_O41_H3,5,TimeData.time_O41_H3, 6, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_H3,5,TimeData.time_O42_H3,6,TimeData.time_O42_R1],
    [1, 5, 7,TimeData.time_O51_H1,8,TimeData.time_O51_H2,9,TimeData.time_O51_H3,10,TimeData.time_O51_H3,11,TimeData.time_O51_H3],
]

use_case_H5R2= [
    [15, 17, 5],
    [3, 5, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3,4,TimeData.time_O11_H3,5,TimeData.time_O11_H3, 7, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_H3,5,TimeData.time_O12_H3,6,TimeData.time_O12_R1,7,TimeData.time_O12_R2, 7, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_H3,5,TimeData.time_O13_H3,6,TimeData.time_O13_R1,7,TimeData.time_O13_R2],
    [3, 5, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3,4,TimeData.time_O21_H3,5,TimeData.time_O21_H3, 7, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_H3,5,TimeData.time_O22_H3,6,TimeData.time_O22_R1,7,TimeData.time_O22_R2, 7, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_H3,5,TimeData.time_O23_H3,6,TimeData.time_O23_R1,7,TimeData.time_O23_R2],
    [2, 5, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3,4,TimeData.time_O31_H3,5,TimeData.time_O31_H3, 7, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_H3,5,TimeData.time_O32_H3,6,TimeData.time_O32_R1,7,TimeData.time_O32_R2],
    [2, 5, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3,4,TimeData.time_O41_H3,5,TimeData.time_O41_H3, 7, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_H3,5,TimeData.time_O42_H3,6,TimeData.time_O42_R1,7,TimeData.time_O42_R2],
    [1, 5, 8,TimeData.time_O51_H1,10,TimeData.time_O51_H2,12,TimeData.time_O51_H3,14,TimeData.time_O51_H3,16,TimeData.time_O51_H3],
    [3, 5, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3,4,TimeData.time_O11_H3,5,TimeData.time_O11_H3, 7, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_H3,5,TimeData.time_O12_H3,6,TimeData.time_O12_R1,7,TimeData.time_O12_R2, 7, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_H3,5,TimeData.time_O13_H3,6,TimeData.time_O13_R1,7,TimeData.time_O13_R2],
    [3, 5, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3,4,TimeData.time_O21_H3,5,TimeData.time_O21_H3, 7, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_H3,5,TimeData.time_O22_H3,6,TimeData.time_O22_R1,7,TimeData.time_O22_R2, 7, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_H3,5,TimeData.time_O23_H3,6,TimeData.time_O23_R1,7,TimeData.time_O23_R2],
    [2, 5, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3,4,TimeData.time_O31_H3,5,TimeData.time_O31_H3, 7, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_H3,5,TimeData.time_O32_H3,6,TimeData.time_O32_R1,7,TimeData.time_O32_R2],
    [2, 5, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3,4,TimeData.time_O41_H3,5,TimeData.time_O41_H3, 7, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_H3,5,TimeData.time_O42_H3,6,TimeData.time_O42_R1,7,TimeData.time_O42_R2],
    [1, 5, 8,TimeData.time_O51_H1,10,TimeData.time_O51_H2,12,TimeData.time_O51_H3,14,TimeData.time_O51_H3,16,TimeData.time_O51_H3],
    [3, 5, 1,TimeData.time_O11_H1,2,TimeData.time_O11_H2,3,TimeData.time_O11_H3,4,TimeData.time_O11_H3,5,TimeData.time_O11_H3, 7, 1,TimeData.time_O12_H1,2,TimeData.time_O12_H2,3,TimeData.time_O12_H3,4,TimeData.time_O12_H3,5,TimeData.time_O12_H3,6,TimeData.time_O12_R1,7,TimeData.time_O12_R2, 7, 1,TimeData.time_O13_H1,2,TimeData.time_O13_H2,3,TimeData.time_O13_H3,4,TimeData.time_O13_H3,5,TimeData.time_O13_H3,6,TimeData.time_O13_R1,7,TimeData.time_O13_R2],
    [3, 5, 1,TimeData.time_O21_H1,2,TimeData.time_O21_H2,3,TimeData.time_O21_H3,4,TimeData.time_O21_H3,5,TimeData.time_O21_H3, 7, 1,TimeData.time_O22_H1,2,TimeData.time_O22_H2,3,TimeData.time_O22_H3,4,TimeData.time_O22_H3,5,TimeData.time_O22_H3,6,TimeData.time_O22_R1,7,TimeData.time_O22_R2, 7, 1,TimeData.time_O23_H1,2,TimeData.time_O23_H2,3,TimeData.time_O23_H3,4,TimeData.time_O23_H3,5,TimeData.time_O23_H3,6,TimeData.time_O23_R1,7,TimeData.time_O23_R2],
    [2, 5, 1,TimeData.time_O31_H1,2,TimeData.time_O31_H2,3,TimeData.time_O31_H3,4,TimeData.time_O31_H3,5,TimeData.time_O31_H3, 7, 1,TimeData.time_O32_H1,2,TimeData.time_O32_H2,3,TimeData.time_O32_H3,4,TimeData.time_O32_H3,5,TimeData.time_O32_H3,6,TimeData.time_O32_R1,7,TimeData.time_O32_R2],
    [2, 5, 1,TimeData.time_O41_H1,2,TimeData.time_O41_H2,3,TimeData.time_O41_H3,4,TimeData.time_O41_H3,5,TimeData.time_O41_H3, 7, 1,TimeData.time_O42_H1,2,TimeData.time_O42_H2,3,TimeData.time_O42_H3,4,TimeData.time_O42_H3,5,TimeData.time_O42_H3,6,TimeData.time_O42_R1,7,TimeData.time_O42_R2],
    [1, 5, 8,TimeData.time_O51_H1,10,TimeData.time_O51_H2,12,TimeData.time_O51_H3,14,TimeData.time_O51_H3,16,TimeData.time_O51_H3],
]

use_case_list = [use_case_H1R1, use_case_H2R2,use_case_H2R4, use_case_H3R1,use_case_H3R3, use_case_H4R1,use_case_H4R2, use_case_H5R1, use_case_H5R2]

for i, instance_type in enumerate(instance_types):
    back_file = "C:\\Users\\jia\\Desktop\\hrcscheduling\\examples_for_hrc\\test_data\\use_case_{instance_type}.pickle".format(instance_type=instance_type)
    if os.path.exists(back_file):
        with open(back_file, 'rb') as file:
            use_case = pickle.load(file)
    else:
        print("No {}, generate pickle".format(instance_type))
        use_case = use_case_list[i]
        for lst in use_case:
            for i in range(len(lst)):
                if isinstance(lst[i], FuzzyNumber):
                    lst[i].sampling()
        with open(back_file, "wb") as file:
            pickle.dump(use_case, file)
        print("Generate {}.pickle".format(instance_type))

    file_path = 'C:\\Users\\jia\\Desktop\\hrcscheduling\\examples_for_hrc\\test_data\\dataset\\{instance_type}\\{instance_type}_{num}.txt'
    for file_index in range(20): 
        use_case_copy = copy.deepcopy(use_case)
        for lst in use_case_copy:
            for k in range(len(lst)):
                if isinstance(lst[k], FuzzyNumber):
                    lst[k] = round(lst[k].random())
        output_list = [sublist for sublist in use_case_copy]
        with open(file_path.format(instance_type=instance_type,num=file_index), 'w') as file:
            for sublist in output_list:
                file.write(' '.join(map(str, sublist)) + '\n')