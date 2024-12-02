import sys
import copy
import pickle
import os
from flexhrc import flexhrc
from time_data import TimeData
from fuzzyNumber import FuzzyNumber

use_case_H3R1 = [
    [   # Job 0
        [(TimeData.time_O11_H1, 0), (TimeData.time_O11_H2, 1), (TimeData.time_O11_H3, 2)], # Task 0
        [(TimeData.time_O12_H1, 0), (TimeData.time_O12_H2, 1), (TimeData.time_O12_H3, 2), (TimeData.time_O12_R1, 3)],# Task 1
        [(TimeData.time_O13_H1, 0), (TimeData.time_O13_H2, 1), (TimeData.time_O13_H3, 2), (TimeData.time_O13_R1, 3)],# Task 2
    ],
    [   # Job 1
        [(TimeData.time_O21_H1, 0), (TimeData.time_O21_H2, 1), (TimeData.time_O21_H3, 2)], # Task 0
        [(TimeData.time_O22_H1, 0), (TimeData.time_O22_H2, 1), (TimeData.time_O22_H3, 2), (TimeData.time_O22_R1, 3)],
        [(TimeData.time_O23_H1, 0), (TimeData.time_O23_H2, 1), (TimeData.time_O23_H3, 2), (TimeData.time_O23_R1, 3)],
    ],
    [   # Job 2
        [(TimeData.time_O31_H1, 0), (TimeData.time_O31_H2, 1), (TimeData.time_O31_H3, 2)], # Task 0
        [(TimeData.time_O32_H1, 0), (TimeData.time_O32_H2, 1), (TimeData.time_O32_H3, 2), (TimeData.time_O32_R1, 3)],
    ],
    [   # Job 3
        [(TimeData.time_O41_H1, 0), (TimeData.time_O41_H2, 1), (TimeData.time_O41_H3, 2)], # Task 0
        [(TimeData.time_O42_H1, 0), (TimeData.time_O42_H2, 1), (TimeData.time_O42_H3, 2), (TimeData.time_O42_R1, 3)],
    ],
    [   # Job 4
        [(TimeData.time_O51_H1, 4), (TimeData.time_O51_H2, 5), (TimeData.time_O51_H3, 6)],
    ],

    [   # Job 0
        [(TimeData.time_O11_H1, 0), (TimeData.time_O11_H2, 1), (TimeData.time_O11_H3, 2)], # Task 0
        [(TimeData.time_O12_H1, 0), (TimeData.time_O12_H2, 1), (TimeData.time_O12_H3, 2), (TimeData.time_O12_R1, 3)],
        [(TimeData.time_O13_H1, 0), (TimeData.time_O13_H2, 1), (TimeData.time_O13_H3, 2), (TimeData.time_O13_R1, 3)],
    ],
    [   # Job 1
        [(TimeData.time_O21_H1, 0), (TimeData.time_O21_H2, 1), (TimeData.time_O21_H3, 2)], # Task 0
        [(TimeData.time_O22_H1, 0), (TimeData.time_O22_H2, 1), (TimeData.time_O22_H3, 2), (TimeData.time_O22_R1, 3)],
        [(TimeData.time_O23_H1, 0), (TimeData.time_O23_H2, 1), (TimeData.time_O23_H3, 2), (TimeData.time_O23_R1, 3)],
    ],
    [   # Job 2
        [(TimeData.time_O31_H1, 0), (TimeData.time_O31_H2, 1), (TimeData.time_O31_H3, 2)], # Task 0
        [(TimeData.time_O32_H1, 0), (TimeData.time_O32_H2, 1), (TimeData.time_O32_H3, 2), (TimeData.time_O32_R1, 3)],
    ],
    [   # Job 3
        [(TimeData.time_O41_H1, 0), (TimeData.time_O41_H2, 1), (TimeData.time_O41_H3, 2)], # Task 0
        [(TimeData.time_O42_H1, 0), (TimeData.time_O42_H2, 1), (TimeData.time_O42_H3, 2), (TimeData.time_O42_R1, 3)],
    ],
    [   # Job 4
        [(TimeData.time_O51_H1, 4), (TimeData.time_O51_H2, 5), (TimeData.time_O51_H3, 6)],
    ],

    [   # Job 0
        [(TimeData.time_O11_H1, 0), (TimeData.time_O11_H2, 1), (TimeData.time_O11_H3, 2)], # Task 0
        [(TimeData.time_O12_H1, 0), (TimeData.time_O12_H2, 1), (TimeData.time_O12_H3, 2), (TimeData.time_O12_R1, 3)],
        [(TimeData.time_O13_H1, 0), (TimeData.time_O13_H2, 1), (TimeData.time_O13_H3, 2), (TimeData.time_O13_R1, 3)],
    ],
    [   # Job 1
        [(TimeData.time_O21_H1, 0), (TimeData.time_O21_H2, 1), (TimeData.time_O21_H3, 2)], # Task 0
        [(TimeData.time_O22_H1, 0), (TimeData.time_O22_H2, 1), (TimeData.time_O22_H3, 2), (TimeData.time_O22_R1, 3)],
        [(TimeData.time_O23_H1, 0), (TimeData.time_O23_H2, 1), (TimeData.time_O23_H3, 2), (TimeData.time_O23_R1, 3)],
    ],
    [   # Job 2
        [(TimeData.time_O31_H1, 0), (TimeData.time_O31_H2, 1), (TimeData.time_O31_H3, 2)], # Task 0
        [(TimeData.time_O32_H1, 0), (TimeData.time_O32_H2, 1), (TimeData.time_O32_H3, 2), (TimeData.time_O32_R1, 3)],
    ],
    [   # Job 3
        [(TimeData.time_O41_H1, 0), (TimeData.time_O41_H2, 1), (TimeData.time_O41_H3, 2)], # Task 0
        [(TimeData.time_O42_H1, 0), (TimeData.time_O42_H2, 1), (TimeData.time_O42_H3, 2), (TimeData.time_O42_R1, 3)],
    ],
    [   # Job 4
        [(TimeData.time_O51_H1, 4), (TimeData.time_O51_H2, 5), (TimeData.time_O51_H3, 6)],
    ],
]

use_case_H4R1 = [
    [   # Job 0
        [(TimeData.time_O11_H1, 0), (TimeData.time_O11_H2, 1), (TimeData.time_O11_H3, 2), (TimeData.time_O11_H3, 3)], # Task 0
        [(TimeData.time_O12_H1, 0), (TimeData.time_O12_H2, 1), (TimeData.time_O12_H3, 2), (TimeData.time_O12_H3, 3), (TimeData.time_O12_R1, 4)],# Task 1
        [(TimeData.time_O13_H1, 0), (TimeData.time_O13_H2, 1), (TimeData.time_O13_H3, 2), (TimeData.time_O13_H3, 3), (TimeData.time_O13_R1, 4)],# Task 2
    ],
    [   # Job 1
        [(TimeData.time_O21_H1, 0), (TimeData.time_O21_H2, 1), (TimeData.time_O21_H3, 2), (TimeData.time_O21_H3, 3)], # Task 0
        [(TimeData.time_O22_H1, 0), (TimeData.time_O22_H2, 1), (TimeData.time_O22_H3, 2), (TimeData.time_O22_H3, 3), (TimeData.time_O22_R1, 4)],
        [(TimeData.time_O23_H1, 0), (TimeData.time_O23_H2, 1), (TimeData.time_O23_H3, 2), (TimeData.time_O23_H3, 3), (TimeData.time_O23_R1, 4)],
    ],
    [   # Job 2
        [(TimeData.time_O31_H1, 0), (TimeData.time_O31_H2, 1), (TimeData.time_O31_H3, 2), (TimeData.time_O31_H3, 3)], # Task 0
        [(TimeData.time_O32_H1, 0), (TimeData.time_O32_H2, 1), (TimeData.time_O32_H3, 2), (TimeData.time_O32_H3, 3), (TimeData.time_O32_R1, 4)],
    ],
    [   # Job 3
        [(TimeData.time_O41_H1, 0), (TimeData.time_O41_H2, 1), (TimeData.time_O41_H3, 2), (TimeData.time_O41_H3, 3)], # Task 0
        [(TimeData.time_O42_H1, 0), (TimeData.time_O42_H2, 1), (TimeData.time_O42_H3, 2), (TimeData.time_O42_H3, 3), (TimeData.time_O42_R1, 4)],
    ],
    [   # Job 4
        [(TimeData.time_O51_H1, 5), (TimeData.time_O51_H2, 6), (TimeData.time_O51_H3, 7), (TimeData.time_O51_H3, 8)],
    ],

    [   # Job 0
        [(TimeData.time_O11_H1, 0), (TimeData.time_O11_H2, 1), (TimeData.time_O11_H3, 2), (TimeData.time_O11_H3, 3)], # Task 0
        [(TimeData.time_O12_H1, 0), (TimeData.time_O12_H2, 1), (TimeData.time_O12_H3, 2), (TimeData.time_O12_H3, 3), (TimeData.time_O12_R1, 4)],# Task 1
        [(TimeData.time_O13_H1, 0), (TimeData.time_O13_H2, 1), (TimeData.time_O13_H3, 2), (TimeData.time_O13_H3, 3), (TimeData.time_O13_R1, 4)],# Task 2
    ],
    [   # Job 1
        [(TimeData.time_O21_H1, 0), (TimeData.time_O21_H2, 1), (TimeData.time_O21_H3, 2), (TimeData.time_O21_H3, 3)], # Task 0
        [(TimeData.time_O22_H1, 0), (TimeData.time_O22_H2, 1), (TimeData.time_O22_H3, 2), (TimeData.time_O22_H3, 3), (TimeData.time_O22_R1, 4)],
        [(TimeData.time_O23_H1, 0), (TimeData.time_O23_H2, 1), (TimeData.time_O23_H3, 2), (TimeData.time_O23_H3, 3), (TimeData.time_O23_R1, 4)],
    ],
    [   # Job 2
        [(TimeData.time_O31_H1, 0), (TimeData.time_O31_H2, 1), (TimeData.time_O31_H3, 2), (TimeData.time_O31_H3, 3)], # Task 0
        [(TimeData.time_O32_H1, 0), (TimeData.time_O32_H2, 1), (TimeData.time_O32_H3, 2), (TimeData.time_O32_H3, 3), (TimeData.time_O32_R1, 4)],
    ],
    [   # Job 3
        [(TimeData.time_O41_H1, 0), (TimeData.time_O41_H2, 1), (TimeData.time_O41_H3, 2), (TimeData.time_O41_H3, 3)], # Task 0
        [(TimeData.time_O42_H1, 0), (TimeData.time_O42_H2, 1), (TimeData.time_O42_H3, 2), (TimeData.time_O42_H3, 3), (TimeData.time_O42_R1, 4)],
    ],
    [   # Job 4
        [(TimeData.time_O51_H1, 5), (TimeData.time_O51_H2, 6), (TimeData.time_O51_H3, 7), (TimeData.time_O51_H3, 8)],
    ],

    [   # Job 0
        [(TimeData.time_O11_H1, 0), (TimeData.time_O11_H2, 1), (TimeData.time_O11_H3, 2), (TimeData.time_O11_H3, 3)], # Task 0
        [(TimeData.time_O12_H1, 0), (TimeData.time_O12_H2, 1), (TimeData.time_O12_H3, 2), (TimeData.time_O12_H3, 3), (TimeData.time_O12_R1, 4)],# Task 1
        [(TimeData.time_O13_H1, 0), (TimeData.time_O13_H2, 1), (TimeData.time_O13_H3, 2), (TimeData.time_O13_H3, 3), (TimeData.time_O13_R1, 4)],# Task 2
    ],
    [   # Job 1
        [(TimeData.time_O21_H1, 0), (TimeData.time_O21_H2, 1), (TimeData.time_O21_H3, 2), (TimeData.time_O21_H3, 3)], # Task 0
        [(TimeData.time_O22_H1, 0), (TimeData.time_O22_H2, 1), (TimeData.time_O22_H3, 2), (TimeData.time_O22_H3, 3), (TimeData.time_O22_R1, 4)],
        [(TimeData.time_O23_H1, 0), (TimeData.time_O23_H2, 1), (TimeData.time_O23_H3, 2), (TimeData.time_O23_H3, 3), (TimeData.time_O23_R1, 4)],
    ],
    [   # Job 2
        [(TimeData.time_O31_H1, 0), (TimeData.time_O31_H2, 1), (TimeData.time_O31_H3, 2), (TimeData.time_O31_H3, 3)], # Task 0
        [(TimeData.time_O32_H1, 0), (TimeData.time_O32_H2, 1), (TimeData.time_O32_H3, 2), (TimeData.time_O32_H3, 3), (TimeData.time_O32_R1, 4)],
    ],
    [   # Job 3
        [(TimeData.time_O41_H1, 0), (TimeData.time_O41_H2, 1), (TimeData.time_O41_H3, 2), (TimeData.time_O41_H3, 3)], # Task 0
        [(TimeData.time_O42_H1, 0), (TimeData.time_O42_H2, 1), (TimeData.time_O42_H3, 2), (TimeData.time_O42_H3, 3), (TimeData.time_O42_R1, 4)],
    ],
    [   # Job 4
        [(TimeData.time_O51_H1, 5), (TimeData.time_O51_H2, 6), (TimeData.time_O51_H3, 7), (TimeData.time_O51_H3, 8)],
    ],
    
]

use_case_H5R1 = [
    [   # Job 0
        [(TimeData.time_O11_H1, 0), (TimeData.time_O11_H2, 1), (TimeData.time_O11_H3, 2), (TimeData.time_O11_H3, 3), (TimeData.time_O11_H3, 4)], # Task 0
        [(TimeData.time_O12_H1, 0), (TimeData.time_O12_H2, 1), (TimeData.time_O12_H3, 2), (TimeData.time_O12_H3, 3), (TimeData.time_O12_H3, 4), (TimeData.time_O12_R1, 5)],# Task 1
        [(TimeData.time_O13_H1, 0), (TimeData.time_O13_H2, 1), (TimeData.time_O13_H3, 2), (TimeData.time_O13_H3, 3), (TimeData.time_O13_H3, 4), (TimeData.time_O13_R1, 5)],# Task 2
    ],
    [   # Job 1
        [(TimeData.time_O21_H1, 0), (TimeData.time_O21_H2, 1), (TimeData.time_O21_H3, 2), (TimeData.time_O21_H3, 3), (TimeData.time_O21_H3, 4)], # Task 0
        [(TimeData.time_O22_H1, 0), (TimeData.time_O22_H2, 1), (TimeData.time_O22_H3, 2), (TimeData.time_O22_H3, 3), (TimeData.time_O22_H3, 4), (TimeData.time_O22_R1, 5)],
        [(TimeData.time_O23_H1, 0), (TimeData.time_O23_H2, 1), (TimeData.time_O23_H3, 2), (TimeData.time_O23_H3, 3), (TimeData.time_O23_H3, 4), (TimeData.time_O23_R1, 5)],
    ],
    [   # Job 2
        [(TimeData.time_O31_H1, 0), (TimeData.time_O31_H2, 1), (TimeData.time_O31_H3, 2), (TimeData.time_O31_H3, 3), (TimeData.time_O31_H3, 4)], # Task 0
        [(TimeData.time_O32_H1, 0), (TimeData.time_O32_H2, 1), (TimeData.time_O32_H3, 2), (TimeData.time_O32_H3, 3), (TimeData.time_O32_H3, 4), (TimeData.time_O32_R1, 5)],
    ],
    [   # Job 3
        [(TimeData.time_O41_H1, 0), (TimeData.time_O41_H2, 1), (TimeData.time_O41_H3, 2), (TimeData.time_O41_H3, 3), (TimeData.time_O41_H3, 4)], # Task 0
        [(TimeData.time_O42_H1, 0), (TimeData.time_O42_H2, 1), (TimeData.time_O42_H3, 2), (TimeData.time_O42_H3, 3), (TimeData.time_O42_H3, 4), (TimeData.time_O42_R1, 5)],
    ],
    [   # Job 4
        [(TimeData.time_O51_H1, 6), (TimeData.time_O51_H2, 7), (TimeData.time_O51_H3, 8), (TimeData.time_O51_H3, 9), (TimeData.time_O51_H3, 10)],
    ],

    [   # Job 0
        [(TimeData.time_O11_H1, 0), (TimeData.time_O11_H2, 1), (TimeData.time_O11_H3, 2), (TimeData.time_O11_H3, 3), (TimeData.time_O11_H3, 4)], # Task 0
        [(TimeData.time_O12_H1, 0), (TimeData.time_O12_H2, 1), (TimeData.time_O12_H3, 2), (TimeData.time_O12_H3, 3), (TimeData.time_O12_H3, 4), (TimeData.time_O12_R1, 5)],# Task 1
        [(TimeData.time_O13_H1, 0), (TimeData.time_O13_H2, 1), (TimeData.time_O13_H3, 2), (TimeData.time_O13_H3, 3), (TimeData.time_O13_H3, 4), (TimeData.time_O13_R1, 5)],# Task 2
    ],
    [   # Job 1
        [(TimeData.time_O21_H1, 0), (TimeData.time_O21_H2, 1), (TimeData.time_O21_H3, 2), (TimeData.time_O21_H3, 3), (TimeData.time_O21_H3, 4)], # Task 0
        [(TimeData.time_O22_H1, 0), (TimeData.time_O22_H2, 1), (TimeData.time_O22_H3, 2), (TimeData.time_O22_H3, 3), (TimeData.time_O22_H3, 4), (TimeData.time_O22_R1, 5)],
        [(TimeData.time_O23_H1, 0), (TimeData.time_O23_H2, 1), (TimeData.time_O23_H3, 2), (TimeData.time_O23_H3, 3), (TimeData.time_O23_H3, 4), (TimeData.time_O23_R1, 5)],
    ],
    [   # Job 2
        [(TimeData.time_O31_H1, 0), (TimeData.time_O31_H2, 1), (TimeData.time_O31_H3, 2), (TimeData.time_O31_H3, 3), (TimeData.time_O31_H3, 4)], # Task 0
        [(TimeData.time_O32_H1, 0), (TimeData.time_O32_H2, 1), (TimeData.time_O32_H3, 2), (TimeData.time_O32_H3, 3), (TimeData.time_O32_H3, 4), (TimeData.time_O32_R1, 5)],
    ],
    [   # Job 3
        [(TimeData.time_O41_H1, 0), (TimeData.time_O41_H2, 1), (TimeData.time_O41_H3, 2), (TimeData.time_O41_H3, 3), (TimeData.time_O41_H3, 4)], # Task 0
        [(TimeData.time_O42_H1, 0), (TimeData.time_O42_H2, 1), (TimeData.time_O42_H3, 2), (TimeData.time_O42_H3, 3), (TimeData.time_O42_H3, 4), (TimeData.time_O42_R1, 5)],
    ],
    [   # Job 4
        [(TimeData.time_O51_H1, 6), (TimeData.time_O51_H2, 7), (TimeData.time_O51_H3, 8), (TimeData.time_O51_H3, 9), (TimeData.time_O51_H3, 10)],
    ],

    [   # Job 0
        [(TimeData.time_O11_H1, 0), (TimeData.time_O11_H2, 1), (TimeData.time_O11_H3, 2), (TimeData.time_O11_H3, 3), (TimeData.time_O11_H3, 4)], # Task 0
        [(TimeData.time_O12_H1, 0), (TimeData.time_O12_H2, 1), (TimeData.time_O12_H3, 2), (TimeData.time_O12_H3, 3), (TimeData.time_O12_H3, 4), (TimeData.time_O12_R1, 5)],# Task 1
        [(TimeData.time_O13_H1, 0), (TimeData.time_O13_H2, 1), (TimeData.time_O13_H3, 2), (TimeData.time_O13_H3, 3), (TimeData.time_O13_H3, 4), (TimeData.time_O13_R1, 5)],# Task 2
    ],
    [   # Job 1
        [(TimeData.time_O21_H1, 0), (TimeData.time_O21_H2, 1), (TimeData.time_O21_H3, 2), (TimeData.time_O21_H3, 3), (TimeData.time_O21_H3, 4)], # Task 0
        [(TimeData.time_O22_H1, 0), (TimeData.time_O22_H2, 1), (TimeData.time_O22_H3, 2), (TimeData.time_O22_H3, 3), (TimeData.time_O22_H3, 4), (TimeData.time_O22_R1, 5)],
        [(TimeData.time_O23_H1, 0), (TimeData.time_O23_H2, 1), (TimeData.time_O23_H3, 2), (TimeData.time_O23_H3, 3), (TimeData.time_O23_H3, 4), (TimeData.time_O23_R1, 5)],
    ],
    [   # Job 2
        [(TimeData.time_O31_H1, 0), (TimeData.time_O31_H2, 1), (TimeData.time_O31_H3, 2), (TimeData.time_O31_H3, 3), (TimeData.time_O31_H3, 4)], # Task 0
        [(TimeData.time_O32_H1, 0), (TimeData.time_O32_H2, 1), (TimeData.time_O32_H3, 2), (TimeData.time_O32_H3, 3), (TimeData.time_O32_H3, 4), (TimeData.time_O32_R1, 5)],
    ],
    [   # Job 3
        [(TimeData.time_O41_H1, 0), (TimeData.time_O41_H2, 1), (TimeData.time_O41_H3, 2), (TimeData.time_O41_H3, 3), (TimeData.time_O41_H3, 4)], # Task 0
        [(TimeData.time_O42_H1, 0), (TimeData.time_O42_H2, 1), (TimeData.time_O42_H3, 2), (TimeData.time_O42_H3, 3), (TimeData.time_O42_H3, 4), (TimeData.time_O42_R1, 5)],
    ],
    [   # Job 4
        [(TimeData.time_O51_H1, 6), (TimeData.time_O51_H2, 7), (TimeData.time_O51_H3, 8), (TimeData.time_O51_H3, 9), (TimeData.time_O51_H3, 10)],
    ],
]

use_case_H5R2= [
    [   # Job 0
        [(TimeData.time_O11_H1, 0), (TimeData.time_O11_H2, 1), (TimeData.time_O11_H3, 2), (TimeData.time_O11_H3, 3), (TimeData.time_O11_H3, 4)], # Task 0
        [(TimeData.time_O12_H1, 0), (TimeData.time_O12_H2, 1), (TimeData.time_O12_H3, 2), (TimeData.time_O12_H3, 3), (TimeData.time_O12_H3, 4), (TimeData.time_O12_R1, 5), (TimeData.time_O12_R2, 6)],# Task 1
        [(TimeData.time_O13_H1, 0), (TimeData.time_O13_H2, 1), (TimeData.time_O13_H3, 2), (TimeData.time_O13_H3, 3), (TimeData.time_O13_H3, 4), (TimeData.time_O13_R1, 5), (TimeData.time_O13_R2, 6)],# Task 2
    ],
    [   # Job 1
        [(TimeData.time_O21_H1, 0), (TimeData.time_O21_H2, 1), (TimeData.time_O21_H3, 2), (TimeData.time_O21_H3, 3), (TimeData.time_O21_H3, 4)], # Task 0
        [(TimeData.time_O22_H1, 0), (TimeData.time_O22_H2, 1), (TimeData.time_O22_H3, 2), (TimeData.time_O22_H3, 3), (TimeData.time_O22_H3, 4), (TimeData.time_O22_R1, 5), (TimeData.time_O22_R2, 6)],
        [(TimeData.time_O23_H1, 0), (TimeData.time_O23_H2, 1), (TimeData.time_O23_H3, 2), (TimeData.time_O23_H3, 3), (TimeData.time_O23_H3, 4), (TimeData.time_O23_R1, 5), (TimeData.time_O23_R2, 6)],
    ],
    [   # Job 2
        [(TimeData.time_O31_H1, 0), (TimeData.time_O31_H2, 1), (TimeData.time_O31_H3, 2), (TimeData.time_O31_H3, 3), (TimeData.time_O31_H3, 4)], # Task 0
        [(TimeData.time_O32_H1, 0), (TimeData.time_O32_H2, 1), (TimeData.time_O32_H3, 2), (TimeData.time_O32_H3, 3), (TimeData.time_O32_H3, 4), (TimeData.time_O32_R1, 5), (TimeData.time_O32_R2, 6)],
    ],
    [   # Job 3
        [(TimeData.time_O41_H1, 0), (TimeData.time_O41_H2, 1), (TimeData.time_O41_H3, 2), (TimeData.time_O41_H3, 3), (TimeData.time_O41_H3, 4)], # Task 0
        [(TimeData.time_O42_H1, 0), (TimeData.time_O42_H2, 1), (TimeData.time_O42_H3, 2), (TimeData.time_O42_H3, 3), (TimeData.time_O42_H3, 4), (TimeData.time_O42_R1, 5), (TimeData.time_O42_R2, 6)],
    ],
    [   # Job 4
        [(TimeData.time_O51_H1, 7), (TimeData.time_O51_H2, 9), (TimeData.time_O51_H3, 11), (TimeData.time_O51_H3, 13), (TimeData.time_O51_H3, 15)],
    ],

    [   # Job 0
        [(TimeData.time_O11_H1, 0), (TimeData.time_O11_H2, 1), (TimeData.time_O11_H3, 2), (TimeData.time_O11_H3, 3), (TimeData.time_O11_H3, 4)], # Task 0
        [(TimeData.time_O12_H1, 0), (TimeData.time_O12_H2, 1), (TimeData.time_O12_H3, 2), (TimeData.time_O12_H3, 3), (TimeData.time_O12_H3, 4), (TimeData.time_O12_R1, 5), (TimeData.time_O12_R2, 6)],# Task 1
        [(TimeData.time_O13_H1, 0), (TimeData.time_O13_H2, 1), (TimeData.time_O13_H3, 2), (TimeData.time_O13_H3, 3), (TimeData.time_O13_H3, 4), (TimeData.time_O13_R1, 5), (TimeData.time_O13_R2, 6)],# Task 2
    ],
    [   # Job 1
        [(TimeData.time_O21_H1, 0), (TimeData.time_O21_H2, 1), (TimeData.time_O21_H3, 2), (TimeData.time_O21_H3, 3), (TimeData.time_O21_H3, 4)], # Task 0
        [(TimeData.time_O22_H1, 0), (TimeData.time_O22_H2, 1), (TimeData.time_O22_H3, 2), (TimeData.time_O22_H3, 3), (TimeData.time_O22_H3, 4), (TimeData.time_O22_R1, 5), (TimeData.time_O22_R2, 6)],
        [(TimeData.time_O23_H1, 0), (TimeData.time_O23_H2, 1), (TimeData.time_O23_H3, 2), (TimeData.time_O23_H3, 3), (TimeData.time_O23_H3, 4), (TimeData.time_O23_R1, 5), (TimeData.time_O23_R2, 6)],
    ],
    [   # Job 2
        [(TimeData.time_O31_H1, 0), (TimeData.time_O31_H2, 1), (TimeData.time_O31_H3, 2), (TimeData.time_O31_H3, 3), (TimeData.time_O31_H3, 4)], # Task 0
        [(TimeData.time_O32_H1, 0), (TimeData.time_O32_H2, 1), (TimeData.time_O32_H3, 2), (TimeData.time_O32_H3, 3), (TimeData.time_O32_H3, 4), (TimeData.time_O32_R1, 5), (TimeData.time_O32_R2, 6)],
    ],
    [   # Job 3
        [(TimeData.time_O41_H1, 0), (TimeData.time_O41_H2, 1), (TimeData.time_O41_H3, 2), (TimeData.time_O41_H3, 3), (TimeData.time_O41_H3, 4)], # Task 0
        [(TimeData.time_O42_H1, 0), (TimeData.time_O42_H2, 1), (TimeData.time_O42_H3, 2), (TimeData.time_O42_H3, 3), (TimeData.time_O42_H3, 4), (TimeData.time_O42_R1, 5), (TimeData.time_O42_R2, 6)],
    ],
    [   # Job 4
        [(TimeData.time_O51_H1, 7), (TimeData.time_O51_H2, 9), (TimeData.time_O51_H3, 11), (TimeData.time_O51_H3, 13), (TimeData.time_O51_H3, 15)],
    ],

    [   # Job 0
        [(TimeData.time_O11_H1, 0), (TimeData.time_O11_H2, 1), (TimeData.time_O11_H3, 2), (TimeData.time_O11_H3, 3), (TimeData.time_O11_H3, 4)], # Task 0
        [(TimeData.time_O12_H1, 0), (TimeData.time_O12_H2, 1), (TimeData.time_O12_H3, 2), (TimeData.time_O12_H3, 3), (TimeData.time_O12_H3, 4), (TimeData.time_O12_R1, 5), (TimeData.time_O12_R2, 6)],# Task 1
        [(TimeData.time_O13_H1, 0), (TimeData.time_O13_H2, 1), (TimeData.time_O13_H3, 2), (TimeData.time_O13_H3, 3), (TimeData.time_O13_H3, 4), (TimeData.time_O13_R1, 5), (TimeData.time_O13_R2, 6)],# Task 2
    ],
    [   # Job 1
        [(TimeData.time_O21_H1, 0), (TimeData.time_O21_H2, 1), (TimeData.time_O21_H3, 2), (TimeData.time_O21_H3, 3), (TimeData.time_O21_H3, 4)], # Task 0
        [(TimeData.time_O22_H1, 0), (TimeData.time_O22_H2, 1), (TimeData.time_O22_H3, 2), (TimeData.time_O22_H3, 3), (TimeData.time_O22_H3, 4), (TimeData.time_O22_R1, 5), (TimeData.time_O22_R2, 6)],
        [(TimeData.time_O23_H1, 0), (TimeData.time_O23_H2, 1), (TimeData.time_O23_H3, 2), (TimeData.time_O23_H3, 3), (TimeData.time_O23_H3, 4), (TimeData.time_O23_R1, 5), (TimeData.time_O23_R2, 6)],
    ],
    [   # Job 2
        [(TimeData.time_O31_H1, 0), (TimeData.time_O31_H2, 1), (TimeData.time_O31_H3, 2), (TimeData.time_O31_H3, 3), (TimeData.time_O31_H3, 4)], # Task 0
        [(TimeData.time_O32_H1, 0), (TimeData.time_O32_H2, 1), (TimeData.time_O32_H3, 2), (TimeData.time_O32_H3, 3), (TimeData.time_O32_H3, 4), (TimeData.time_O32_R1, 5), (TimeData.time_O32_R2, 6)],
    ],
    [   # Job 3
        [(TimeData.time_O41_H1, 0), (TimeData.time_O41_H2, 1), (TimeData.time_O41_H3, 2), (TimeData.time_O41_H3, 3), (TimeData.time_O41_H3, 4)], # Task 0
        [(TimeData.time_O42_H1, 0), (TimeData.time_O42_H2, 1), (TimeData.time_O42_H3, 2), (TimeData.time_O42_H3, 3), (TimeData.time_O42_H3, 4), (TimeData.time_O42_R1, 5), (TimeData.time_O42_R2, 6)],
    ],
    [   # Job 4
        [(TimeData.time_O51_H1, 7), (TimeData.time_O51_H2, 9), (TimeData.time_O51_H3, 11), (TimeData.time_O51_H3, 13), (TimeData.time_O51_H3, 15)],
    ],
]

def convert_to_os_ms(scheduling_data, time_data):
    os_sequence = []
    ms_sequence = []

    # 提取任务并按开始时间排序
    tasks = []
    for job, operations in scheduling_data.items():
        for task in operations:
            task_id, start_time, machine = task
            tasks.append((task_id, start_time, machine))

    # 按照任务的开始时间进行排序
    tasks.sort(key=lambda x: x[1])

    # 生成OS和MS编码
    for task in tasks:
        os_sequence.append(task[0])  # OS编码为任务ID
        ms_sequence.append(task[2])  # MS编码为机器编号
    os_part = []
    for task in os_sequence:
        parts = task.split('_')
        jobs = int(parts[1])
        ops = int(parts[2])
        num = 0
        for i, job in zip(range(jobs), time_data):
            num += len(job)
        num += ops+1
        os_part.append(num - 1)
    sorted_indices = sorted(range(len(os_part)), key=lambda k: os_part[k])
    ms_part = [ms_sequence[i] for i in sorted_indices]
    return os_part, ms_part

HandR = [TimeData.time_O51_H1,TimeData.time_O51_H2,TimeData.time_O51_H3]

instance_types = [
    "H3R1", 
    "H4R1", 
    "H5R1", 
    "H5R2"
    ]
use_case_list = [use_case_H3R1, use_case_H4R1, use_case_H5R1, use_case_H5R2]

for i, instance_type in enumerate(instance_types):
    back_file = r"./use_case_{instance_type}.pickle".format(instance_type=instance_type)
    if os.path.exists(back_file):
        with open(back_file, 'rb') as file:
            use_case = pickle.load(file)
    else:
        use_case = use_case_list[i]
        for job in use_case:
            for task in job: 
                for j in range(0, len(task)): 
                    element = task[j][0]
                    if isinstance(element, FuzzyNumber):
                        task[j][0].sampling()
        with open(back_file, "wb") as file:
            pickle.dump(use_case, file)

    fitness = []
    CHS_list = []
    for time in range(100): 
        use_case_copy = copy.deepcopy(use_case)
        for job in use_case_copy:
            for task in job: 
                for k in range(0, len(task)): 
                    element = task[k][0]
                    if isinstance(element, FuzzyNumber):
                        task_list = list(task[k])
                        task_list[0] = round(task_list[0].random()) 
                        task[k] = tuple(task_list) 
        result, scheduling_data = flexhrc(use_case_copy, int(instance_type[1]), int(instance_type[3]))
        fitness.append(result)
        os_part, ms_part = convert_to_os_ms(scheduling_data, use_case_list[i])
        CHS = [ms_part, os_part]
        CHS_list.append(CHS)
    print("{}:{}".format(instance_type, [min(fitness), sum(fitness) / len(fitness), max(fitness)]))
    path = "./" + instance_type[:2] + "/" + instance_type + "/" + "{mean}-testdata.pickle".format(mean=round(sum(fitness) / len(fitness)))
    with open(path, "wb") as file:
        pickle.dump(CHS_list, file)
