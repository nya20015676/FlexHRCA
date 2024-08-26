import sys

from time_data_TFN import TimeData

class TIME_TABLE:
    Time_H1R1 = [
        [TimeData.time_O11_H1, TimeData.time_O11_R1, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_R1, 9999],
        # Tighten 4 screws of right side
        [TimeData.time_O13_H1, TimeData.time_O13_R1, 9999],

        [TimeData.time_O21_H1, TimeData.time_O21_R1, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_R1, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_R1, 9999],

        [TimeData.time_O31_H1, TimeData.time_O31_R1, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_R1, 9999],
        
        [TimeData.time_O41_H1, TimeData.time_O41_R1, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_R1, 9999],

        [9999, 9999, TimeData.time_O51_H1],
    ]

    Time_H1R2 = [
        [TimeData.time_O11_H1, TimeData.time_O11_R1, TimeData.time_O11_R2, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_R1, TimeData.time_O12_R2, 9999, 9999],
        # Tighten 4 screws of right side
        [TimeData.time_O13_H1, TimeData.time_O13_R1, TimeData.time_O13_R2, 9999, 9999],

        [TimeData.time_O21_H1, TimeData.time_O21_R1, TimeData.time_O21_R2, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_R1, TimeData.time_O22_R2, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_R1, TimeData.time_O23_R2, 9999, 9999],

        [TimeData.time_O31_H1, TimeData.time_O31_R1, TimeData.time_O31_R2, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_R1, TimeData.time_O32_R2, 9999, 9999],
        
        [TimeData.time_O41_H1, TimeData.time_O41_R1, TimeData.time_O41_R2, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_R1, TimeData.time_O42_R2, 9999, 9999],

        [9999, 9999, 9999, TimeData.time_O51_H1, 9999],
    ]

    Time_H1R3 = [
        [TimeData.time_O11_H1, TimeData.time_O11_R1, TimeData.time_O11_R2, TimeData.time_O11_R3, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_R1, TimeData.time_O12_R2, TimeData.time_O12_R3, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_R1, TimeData.time_O13_R2, TimeData.time_O13_R3, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_R1, TimeData.time_O21_R2, TimeData.time_O21_R3, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_R1, TimeData.time_O22_R2, TimeData.time_O22_R3, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_R1, TimeData.time_O23_R2, TimeData.time_O23_R3, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_R1, TimeData.time_O31_R2, TimeData.time_O31_R3, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_R1, TimeData.time_O32_R2, TimeData.time_O32_R3, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_R1, TimeData.time_O41_R2, TimeData.time_O41_R3, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_R1, TimeData.time_O42_R2, TimeData.time_O42_R3, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, 9999],
    ]

    Time_H1R4 = [
        [TimeData.time_O11_H1, TimeData.time_O11_R1, TimeData.time_O11_R2, TimeData.time_O11_R3, TimeData.time_O11_R3, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_R1, TimeData.time_O12_R2, TimeData.time_O12_R3, TimeData.time_O12_R3, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_R1, TimeData.time_O13_R2, TimeData.time_O13_R3, TimeData.time_O13_R3, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_R1, TimeData.time_O21_R2, TimeData.time_O21_R3, TimeData.time_O21_R3, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_R1, TimeData.time_O22_R2, TimeData.time_O22_R3, TimeData.time_O22_R3, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_R1, TimeData.time_O23_R2, TimeData.time_O23_R3, TimeData.time_O23_R3, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_R1, TimeData.time_O31_R2, TimeData.time_O31_R3, TimeData.time_O31_R3, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_R1, TimeData.time_O32_R2, TimeData.time_O32_R3, TimeData.time_O32_R3, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_R1, TimeData.time_O41_R2, TimeData.time_O41_R3, TimeData.time_O41_R3, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_R1, TimeData.time_O42_R2, TimeData.time_O42_R3, TimeData.time_O42_R3, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, 9999, 9999],
    ]

    Time_H1R5 = [
        [TimeData.time_O11_H1, TimeData.time_O11_R1, TimeData.time_O11_R2, TimeData.time_O11_R3, TimeData.time_O11_R3, TimeData.time_O11_R3, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_R1, TimeData.time_O12_R2, TimeData.time_O12_R3, TimeData.time_O12_R3, TimeData.time_O12_R3, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_R1, TimeData.time_O13_R2, TimeData.time_O13_R3, TimeData.time_O13_R3, TimeData.time_O13_R3, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_R1, TimeData.time_O21_R2, TimeData.time_O21_R3, TimeData.time_O21_R3, TimeData.time_O21_R3, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_R1, TimeData.time_O22_R2, TimeData.time_O22_R3, TimeData.time_O22_R3, TimeData.time_O22_R3, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_R1, TimeData.time_O23_R2, TimeData.time_O23_R3, TimeData.time_O23_R3, TimeData.time_O23_R3, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_R1, TimeData.time_O31_R2, TimeData.time_O31_R3, TimeData.time_O31_R3, TimeData.time_O31_R3, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_R1, TimeData.time_O32_R2, TimeData.time_O32_R3, TimeData.time_O32_R3, TimeData.time_O32_R3, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_R1, TimeData.time_O41_R2, TimeData.time_O41_R3, TimeData.time_O41_R3, TimeData.time_O41_R3, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_R1, TimeData.time_O42_R2, TimeData.time_O42_R3, TimeData.time_O42_R3, TimeData.time_O42_R3, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, 9999, 9999, 9999],
    ]

    Time_H2R1 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_R1, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_R1, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_R1, 9999, 9999],

        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_R1, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_R1, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_R1, 9999, 9999],

        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_R1, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_R1, 9999, 9999],
        
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_R1, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_R1, 9999, 9999],

        [9999, 9999, 9999, TimeData.time_O51_H1, 9999],
    ]

    Time_H2R2 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_R1, TimeData.time_O11_R2, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_R1, TimeData.time_O12_R2, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_R1, TimeData.time_O13_R2, 9999, 9999, 9999, 9999],

        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_R1, TimeData.time_O21_R2, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_R1, TimeData.time_O22_R2, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_R1, TimeData.time_O23_R2, 9999, 9999, 9999, 9999],

        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_R1, TimeData.time_O31_R2, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_R1, TimeData.time_O32_R2, 9999, 9999, 9999, 9999],
        
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_R1, TimeData.time_O41_R2, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_R1, TimeData.time_O42_R2, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, TimeData.time_O51_H2, 9999],
    ]

    Time_H2R3 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_R1, TimeData.time_O11_R2, TimeData.time_O11_R3, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_R1, TimeData.time_O12_R2, TimeData.time_O12_R3, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_R1, TimeData.time_O13_R2, TimeData.time_O13_R3, 9999, 9999, 9999, 9999, 9999, 9999],

        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_R1, TimeData.time_O21_R2, TimeData.time_O21_R3, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_R1, TimeData.time_O22_R2, TimeData.time_O22_R3, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_R1, TimeData.time_O23_R2, TimeData.time_O23_R3, 9999, 9999, 9999, 9999, 9999, 9999],

        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_R1, TimeData.time_O31_R2, TimeData.time_O31_R3, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_R1, TimeData.time_O32_R2, TimeData.time_O32_R3, 9999, 9999, 9999, 9999, 9999, 9999],
        
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_R1, TimeData.time_O41_R2, TimeData.time_O41_R3, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_R1, TimeData.time_O42_R2, TimeData.time_O42_R3, 9999, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, 9999, TimeData.time_O51_H2, 9999, 9999],
    ]

    Time_H2R4 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_R1, TimeData.time_O11_R2, TimeData.time_O11_R3, TimeData.time_O11_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_R1, TimeData.time_O12_R2, TimeData.time_O12_R3, TimeData.time_O12_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_R1, TimeData.time_O13_R2, TimeData.time_O13_R3, TimeData.time_O13_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_R1, TimeData.time_O21_R2, TimeData.time_O21_R3, TimeData.time_O21_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_R1, TimeData.time_O22_R2, TimeData.time_O22_R3, TimeData.time_O22_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_R1, TimeData.time_O23_R2, TimeData.time_O23_R3, TimeData.time_O23_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_R1, TimeData.time_O31_R2, TimeData.time_O31_R3, TimeData.time_O31_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_R1, TimeData.time_O32_R2, TimeData.time_O32_R3, TimeData.time_O32_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_R1, TimeData.time_O41_R2, TimeData.time_O41_R3, TimeData.time_O41_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_R1, TimeData.time_O42_R2, TimeData.time_O42_R3, TimeData.time_O42_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, 9999, 9999, TimeData.time_O51_H2, 9999, 9999, 9999],
    ]

    Time_H2R5 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_R1, TimeData.time_O11_R2, TimeData.time_O11_R3, TimeData.time_O11_R3, TimeData.time_O11_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_R1, TimeData.time_O12_R2, TimeData.time_O12_R3, TimeData.time_O12_R3, TimeData.time_O12_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_R1, TimeData.time_O13_R2, TimeData.time_O13_R3, TimeData.time_O13_R3, TimeData.time_O13_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_R1, TimeData.time_O21_R2, TimeData.time_O21_R3, TimeData.time_O21_R3, TimeData.time_O21_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_R1, TimeData.time_O22_R2, TimeData.time_O22_R3, TimeData.time_O22_R3, TimeData.time_O22_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_R1, TimeData.time_O23_R2, TimeData.time_O23_R3, TimeData.time_O23_R3, TimeData.time_O23_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_R1, TimeData.time_O31_R2, TimeData.time_O31_R3, TimeData.time_O31_R3, TimeData.time_O31_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_R1, TimeData.time_O32_R2, TimeData.time_O32_R3, TimeData.time_O32_R3, TimeData.time_O32_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_R1, TimeData.time_O41_R2, TimeData.time_O41_R3, TimeData.time_O41_R3, TimeData.time_O41_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_R1, TimeData.time_O42_R2, TimeData.time_O42_R3, TimeData.time_O42_R3, TimeData.time_O42_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, 9999, 9999, 9999, TimeData.time_O51_H2, 9999, 9999, 9999, 9999],
    ]

    Time_H3R1 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_H3,  TimeData.time_O11_R1, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_H3,  TimeData.time_O12_R1, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_H3,  TimeData.time_O13_R1, 9999, 9999, 9999],

        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_H3,  TimeData.time_O21_R1, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_H3,  TimeData.time_O22_R1, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_H3,  TimeData.time_O23_R1, 9999, 9999, 9999],

        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_H3,  TimeData.time_O31_R1, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_H3,  TimeData.time_O32_R1, 9999, 9999, 9999],
        
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_H3,  TimeData.time_O41_R1, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_H3,  TimeData.time_O42_R1, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, TimeData.time_O51_H1, TimeData.time_O51_H2, TimeData.time_O51_H3],
    ]

    Time_H3R2 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_H3,  TimeData.time_O11_R1, TimeData.time_O11_R2, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_H3,  TimeData.time_O12_R1, TimeData.time_O12_R2, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_H3,  TimeData.time_O13_R1, TimeData.time_O13_R2, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_H3,  TimeData.time_O21_R1, TimeData.time_O21_R2, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_H3,  TimeData.time_O22_R1, TimeData.time_O22_R2, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_H3,  TimeData.time_O23_R1, TimeData.time_O23_R2, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_H3,  TimeData.time_O31_R1, TimeData.time_O31_R2, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_H3,  TimeData.time_O32_R1, TimeData.time_O32_R2, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_H3,  TimeData.time_O41_R1, TimeData.time_O41_R2, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_H3,  TimeData.time_O42_R1, TimeData.time_O42_R2, 9999, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, TimeData.time_O51_H2, 9999, TimeData.time_O51_H3, 9999],
    ]

    Time_H3R3 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_H3,  TimeData.time_O11_R1, TimeData.time_O11_R2, TimeData.time_O11_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_H3,  TimeData.time_O12_R1, TimeData.time_O12_R2, TimeData.time_O12_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_H3,  TimeData.time_O13_R1, TimeData.time_O13_R2, TimeData.time_O13_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_H3,  TimeData.time_O21_R1, TimeData.time_O21_R2, TimeData.time_O21_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_H3,  TimeData.time_O22_R1, TimeData.time_O22_R2, TimeData.time_O22_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_H3,  TimeData.time_O23_R1, TimeData.time_O23_R2, TimeData.time_O23_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_H3,  TimeData.time_O31_R1, TimeData.time_O31_R2, TimeData.time_O31_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_H3,  TimeData.time_O32_R1, TimeData.time_O32_R2, TimeData.time_O32_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_H3,  TimeData.time_O41_R1, TimeData.time_O41_R2, TimeData.time_O41_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_H3,  TimeData.time_O42_R1, TimeData.time_O42_R2, TimeData.time_O42_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, 9999, TimeData.time_O51_H2, 9999, 9999, TimeData.time_O51_H3, 9999, 9999],
    ]

    Time_H3R4 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_H3,  TimeData.time_O11_R1, TimeData.time_O11_R2, TimeData.time_O11_R3, TimeData.time_O11_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_H3,  TimeData.time_O12_R1, TimeData.time_O12_R2, TimeData.time_O12_R3, TimeData.time_O12_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_H3,  TimeData.time_O13_R1, TimeData.time_O13_R2, TimeData.time_O13_R3, TimeData.time_O13_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_H3,  TimeData.time_O21_R1, TimeData.time_O21_R2, TimeData.time_O21_R3, TimeData.time_O21_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_H3,  TimeData.time_O22_R1, TimeData.time_O22_R2, TimeData.time_O22_R3, TimeData.time_O22_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_H3,  TimeData.time_O23_R1, TimeData.time_O23_R2, TimeData.time_O23_R3, TimeData.time_O23_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_H3,  TimeData.time_O31_R1, TimeData.time_O31_R2, TimeData.time_O31_R3, TimeData.time_O31_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_H3,  TimeData.time_O32_R1, TimeData.time_O32_R2, TimeData.time_O32_R3, TimeData.time_O32_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_H3,  TimeData.time_O41_R1, TimeData.time_O41_R2, TimeData.time_O41_R3, TimeData.time_O41_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_H3,  TimeData.time_O42_R1, TimeData.time_O42_R2, TimeData.time_O42_R3, TimeData.time_O42_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, 9999, 9999, TimeData.time_O51_H2, 9999, 9999, 9999, TimeData.time_O51_H3, 9999, 9999, 9999],
    ]

    Time_H3R5 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_H3,  TimeData.time_O11_R1, TimeData.time_O11_R2, TimeData.time_O11_R3, TimeData.time_O11_R3, TimeData.time_O11_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_H3,  TimeData.time_O12_R1, TimeData.time_O12_R2, TimeData.time_O12_R3, TimeData.time_O12_R3, TimeData.time_O12_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_H3,  TimeData.time_O13_R1, TimeData.time_O13_R2, TimeData.time_O13_R3, TimeData.time_O13_R3, TimeData.time_O13_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_H3,  TimeData.time_O21_R1, TimeData.time_O21_R2, TimeData.time_O21_R3, TimeData.time_O21_R3, TimeData.time_O21_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_H3,  TimeData.time_O22_R1, TimeData.time_O22_R2, TimeData.time_O22_R3, TimeData.time_O22_R3, TimeData.time_O22_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_H3,  TimeData.time_O23_R1, TimeData.time_O23_R2, TimeData.time_O23_R3, TimeData.time_O23_R3, TimeData.time_O23_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_H3,  TimeData.time_O31_R1, TimeData.time_O31_R2, TimeData.time_O31_R3, TimeData.time_O31_R3, TimeData.time_O31_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_H3,  TimeData.time_O32_R1, TimeData.time_O32_R2, TimeData.time_O32_R3, TimeData.time_O32_R3, TimeData.time_O32_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_H3,  TimeData.time_O41_R1, TimeData.time_O41_R2, TimeData.time_O41_R3, TimeData.time_O41_R3, TimeData.time_O41_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_H3,  TimeData.time_O42_R1, TimeData.time_O42_R2, TimeData.time_O42_R3, TimeData.time_O42_R3, TimeData.time_O42_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, 9999, 9999, 9999, TimeData.time_O51_H2, 9999, 9999, 9999, 9999, TimeData.time_O51_H3, 9999, 9999, 9999, 9999],
    ]

    Time_H3R5 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_H3,  TimeData.time_O11_R1, TimeData.time_O11_R2, TimeData.time_O11_R3, TimeData.time_O11_R3, TimeData.time_O11_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_H3,  TimeData.time_O12_R1, TimeData.time_O12_R2, TimeData.time_O12_R3, TimeData.time_O12_R3, TimeData.time_O12_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_H3,  TimeData.time_O13_R1, TimeData.time_O13_R2, TimeData.time_O13_R3, TimeData.time_O13_R3, TimeData.time_O13_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_H3,  TimeData.time_O21_R1, TimeData.time_O21_R2, TimeData.time_O21_R3, TimeData.time_O21_R3, TimeData.time_O21_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_H3,  TimeData.time_O22_R1, TimeData.time_O22_R2, TimeData.time_O22_R3, TimeData.time_O22_R3, TimeData.time_O22_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_H3,  TimeData.time_O23_R1, TimeData.time_O23_R2, TimeData.time_O23_R3, TimeData.time_O23_R3, TimeData.time_O23_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_H3,  TimeData.time_O31_R1, TimeData.time_O31_R2, TimeData.time_O31_R3, TimeData.time_O31_R3, TimeData.time_O31_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_H3,  TimeData.time_O32_R1, TimeData.time_O32_R2, TimeData.time_O32_R3, TimeData.time_O32_R3, TimeData.time_O32_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_H3,  TimeData.time_O41_R1, TimeData.time_O41_R2, TimeData.time_O41_R3, TimeData.time_O41_R3, TimeData.time_O41_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_H3,  TimeData.time_O42_R1, TimeData.time_O42_R2, TimeData.time_O42_R3, TimeData.time_O42_R3, TimeData.time_O42_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, 9999, 9999, 9999, TimeData.time_O51_H2, 9999, 9999, 9999, 9999, TimeData.time_O51_H3, 9999, 9999, 9999, 9999],
    ]

    Time_H4R1 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_H3, TimeData.time_O11_H3, TimeData.time_O11_R1, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_H3, TimeData.time_O12_H3, TimeData.time_O12_R1, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_H3, TimeData.time_O13_H3, TimeData.time_O13_R1, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_H3, TimeData.time_O21_H3, TimeData.time_O21_R1, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_H3, TimeData.time_O22_H3, TimeData.time_O22_R1, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_H3, TimeData.time_O23_H3, TimeData.time_O23_R1, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_H3, TimeData.time_O31_H3, TimeData.time_O31_R1, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_H3, TimeData.time_O32_H3, TimeData.time_O32_R1, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_H3, TimeData.time_O41_H3, TimeData.time_O41_R1, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_H3, TimeData.time_O42_H3, TimeData.time_O42_R1, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, TimeData.time_O51_H2, TimeData.time_O51_H3, TimeData.time_O51_H3],
    ]

    Time_H4R2 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_H3, TimeData.time_O11_H3, TimeData.time_O11_R1, TimeData.time_O11_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_H3, TimeData.time_O12_H3, TimeData.time_O12_R1, TimeData.time_O12_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_H3, TimeData.time_O13_H3, TimeData.time_O13_R1, TimeData.time_O13_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_H3, TimeData.time_O21_H3, TimeData.time_O21_R1, TimeData.time_O21_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_H3, TimeData.time_O22_H3, TimeData.time_O22_R1, TimeData.time_O22_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_H3, TimeData.time_O23_H3, TimeData.time_O23_R1, TimeData.time_O23_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_H3, TimeData.time_O31_H3, TimeData.time_O31_R1, TimeData.time_O31_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_H3, TimeData.time_O32_H3, TimeData.time_O32_R1, TimeData.time_O32_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_H3, TimeData.time_O41_H3, TimeData.time_O41_R1, TimeData.time_O41_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_H3, TimeData.time_O42_H3, TimeData.time_O42_R1, TimeData.time_O42_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, TimeData.time_O51_H2, 9999, TimeData.time_O51_H3, 9999, TimeData.time_O51_H3, 9999],
    ]

    Time_H4R3 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_H3, TimeData.time_O11_H3, TimeData.time_O11_R1, TimeData.time_O11_R2, TimeData.time_O11_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_H3, TimeData.time_O12_H3, TimeData.time_O12_R1, TimeData.time_O12_R2, TimeData.time_O12_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_H3, TimeData.time_O13_H3, TimeData.time_O13_R1, TimeData.time_O13_R2, TimeData.time_O13_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_H3, TimeData.time_O21_H3, TimeData.time_O21_R1, TimeData.time_O21_R2, TimeData.time_O21_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_H3, TimeData.time_O22_H3, TimeData.time_O22_R1, TimeData.time_O22_R2, TimeData.time_O22_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_H3, TimeData.time_O23_H3, TimeData.time_O23_R1, TimeData.time_O23_R2, TimeData.time_O23_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_H3, TimeData.time_O31_H3, TimeData.time_O31_R1, TimeData.time_O31_R2, TimeData.time_O31_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_H3, TimeData.time_O32_H3, TimeData.time_O32_R1, TimeData.time_O32_R2, TimeData.time_O32_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_H3, TimeData.time_O41_H3, TimeData.time_O41_R1, TimeData.time_O41_R2, TimeData.time_O41_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_H3, TimeData.time_O42_H3, TimeData.time_O42_R1, TimeData.time_O42_R2, TimeData.time_O42_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, 9999, TimeData.time_O51_H2, 9999, 9999, TimeData.time_O51_H3, 9999, 9999, TimeData.time_O51_H3, 9999, 9999],
    ]

    Time_H4R4 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_H3, TimeData.time_O11_H3, TimeData.time_O11_R1, TimeData.time_O11_R2, TimeData.time_O11_R3, TimeData.time_O11_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_H3, TimeData.time_O12_H3, TimeData.time_O12_R1, TimeData.time_O12_R2, TimeData.time_O12_R3, TimeData.time_O12_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_H3, TimeData.time_O13_H3, TimeData.time_O13_R1, TimeData.time_O13_R2, TimeData.time_O13_R3, TimeData.time_O13_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_H3, TimeData.time_O21_H3, TimeData.time_O21_R1, TimeData.time_O21_R2, TimeData.time_O21_R3, TimeData.time_O21_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_H3, TimeData.time_O22_H3, TimeData.time_O22_R1, TimeData.time_O22_R2, TimeData.time_O22_R3, TimeData.time_O22_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_H3, TimeData.time_O23_H3, TimeData.time_O23_R1, TimeData.time_O23_R2, TimeData.time_O23_R3, TimeData.time_O23_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_H3, TimeData.time_O31_H3, TimeData.time_O31_R1, TimeData.time_O31_R2, TimeData.time_O31_R3, TimeData.time_O31_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_H3, TimeData.time_O32_H3, TimeData.time_O32_R1, TimeData.time_O32_R2, TimeData.time_O32_R3, TimeData.time_O32_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_H3, TimeData.time_O41_H3, TimeData.time_O41_R1, TimeData.time_O41_R2, TimeData.time_O41_R3, TimeData.time_O41_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_H3, TimeData.time_O42_H3, TimeData.time_O42_R1, TimeData.time_O42_R2, TimeData.time_O42_R3, TimeData.time_O42_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, 9999, 9999, TimeData.time_O51_H2, 9999, 9999, 9999, TimeData.time_O51_H3, 9999, 9999, 9999, TimeData.time_O51_H3, 9999, 9999, 9999],
    ]

    Time_H4R5 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_H3, TimeData.time_O11_H3, TimeData.time_O11_R1, TimeData.time_O11_R2, TimeData.time_O11_R3, TimeData.time_O11_R3, TimeData.time_O11_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_H3, TimeData.time_O12_H3, TimeData.time_O12_R1, TimeData.time_O12_R2, TimeData.time_O12_R3, TimeData.time_O12_R3, TimeData.time_O12_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_H3, TimeData.time_O13_H3, TimeData.time_O13_R1, TimeData.time_O13_R2, TimeData.time_O13_R3, TimeData.time_O13_R3, TimeData.time_O13_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_H3, TimeData.time_O21_H3, TimeData.time_O21_R1, TimeData.time_O21_R2, TimeData.time_O21_R3, TimeData.time_O21_R3, TimeData.time_O21_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_H3, TimeData.time_O22_H3, TimeData.time_O22_R1, TimeData.time_O22_R2, TimeData.time_O22_R3, TimeData.time_O22_R3, TimeData.time_O22_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_H3, TimeData.time_O23_H3, TimeData.time_O23_R1, TimeData.time_O23_R2, TimeData.time_O23_R3, TimeData.time_O23_R3, TimeData.time_O23_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_H3, TimeData.time_O31_H3, TimeData.time_O31_R1, TimeData.time_O31_R2, TimeData.time_O31_R3, TimeData.time_O31_R3, TimeData.time_O31_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_H3, TimeData.time_O32_H3, TimeData.time_O32_R1, TimeData.time_O32_R2, TimeData.time_O32_R3, TimeData.time_O32_R3, TimeData.time_O32_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_H3, TimeData.time_O41_H3, TimeData.time_O41_R1, TimeData.time_O41_R2, TimeData.time_O41_R3, TimeData.time_O41_R3, TimeData.time_O41_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_H3, TimeData.time_O42_H3, TimeData.time_O42_R1, TimeData.time_O42_R2, TimeData.time_O42_R3, TimeData.time_O42_R3, TimeData.time_O42_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, 9999, 9999, 9999, TimeData.time_O51_H2, 9999, 9999, 9999, 9999, TimeData.time_O51_H3, 9999, 9999, 9999, 9999, TimeData.time_O51_H3, 9999, 9999, 9999, 9999],
    ]

    Time_H5R1 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_H3, TimeData.time_O11_H3, TimeData.time_O11_H3, TimeData.time_O11_R1, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_H3, TimeData.time_O12_H3, TimeData.time_O12_H3, TimeData.time_O12_R1, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_H3, TimeData.time_O13_H3, TimeData.time_O13_H3, TimeData.time_O13_R1, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_H3, TimeData.time_O21_H3, TimeData.time_O21_H3, TimeData.time_O21_R1, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_H3, TimeData.time_O22_H3, TimeData.time_O22_H3, TimeData.time_O22_R1, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_H3, TimeData.time_O23_H3, TimeData.time_O23_H3, TimeData.time_O23_R1, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_H3, TimeData.time_O31_H3, TimeData.time_O31_H3, TimeData.time_O31_R1, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_H3, TimeData.time_O32_H3, TimeData.time_O32_H3, TimeData.time_O32_R1, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_H3, TimeData.time_O41_H3, TimeData.time_O41_H3, TimeData.time_O41_R1, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_H3, TimeData.time_O42_H3, TimeData.time_O42_H3, TimeData.time_O42_R1, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, TimeData.time_O51_H2, TimeData.time_O51_H3, TimeData.time_O51_H3, TimeData.time_O51_H3],
    ]

    Time_H5R2 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_H3, TimeData.time_O11_H3, TimeData.time_O11_H3, TimeData.time_O11_R1, TimeData.time_O11_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_H3, TimeData.time_O12_H3, TimeData.time_O12_H3, TimeData.time_O12_R1, TimeData.time_O12_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_H3, TimeData.time_O13_H3, TimeData.time_O13_H3, TimeData.time_O13_R1, TimeData.time_O13_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_H3, TimeData.time_O21_H3, TimeData.time_O21_H3, TimeData.time_O21_R1, TimeData.time_O21_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_H3, TimeData.time_O22_H3, TimeData.time_O22_H3, TimeData.time_O22_R1, TimeData.time_O22_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_H3, TimeData.time_O23_H3, TimeData.time_O23_H3, TimeData.time_O23_R1, TimeData.time_O23_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_H3, TimeData.time_O31_H3, TimeData.time_O31_H3, TimeData.time_O31_R1, TimeData.time_O31_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_H3, TimeData.time_O32_H3, TimeData.time_O32_H3, TimeData.time_O32_R1, TimeData.time_O32_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_H3, TimeData.time_O41_H3, TimeData.time_O41_H3, TimeData.time_O41_R1, TimeData.time_O41_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_H3, TimeData.time_O42_H3, TimeData.time_O42_H3, TimeData.time_O42_R1, TimeData.time_O42_R2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, TimeData.time_O51_H2, 9999, TimeData.time_O51_H3, 9999, TimeData.time_O51_H3, 9999, TimeData.time_O51_H3, 9999],
    ]

    Time_H5R3 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_H3, TimeData.time_O11_H3, TimeData.time_O11_H3, TimeData.time_O11_R1, TimeData.time_O11_R2, TimeData.time_O11_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_H3, TimeData.time_O12_H3, TimeData.time_O12_H3, TimeData.time_O12_R1, TimeData.time_O12_R2, TimeData.time_O12_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_H3, TimeData.time_O13_H3, TimeData.time_O13_H3, TimeData.time_O13_R1, TimeData.time_O13_R2, TimeData.time_O13_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_H3, TimeData.time_O21_H3, TimeData.time_O21_H3, TimeData.time_O21_R1, TimeData.time_O21_R2, TimeData.time_O21_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_H3, TimeData.time_O22_H3, TimeData.time_O22_H3, TimeData.time_O22_R1, TimeData.time_O22_R2, TimeData.time_O22_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_H3, TimeData.time_O23_H3, TimeData.time_O23_H3, TimeData.time_O23_R1, TimeData.time_O23_R2, TimeData.time_O23_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_H3, TimeData.time_O31_H3, TimeData.time_O31_H3, TimeData.time_O31_R1, TimeData.time_O31_R2, TimeData.time_O31_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_H3, TimeData.time_O32_H3, TimeData.time_O32_H3, TimeData.time_O32_R1, TimeData.time_O32_R2, TimeData.time_O32_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_H3, TimeData.time_O41_H3, TimeData.time_O41_H3, TimeData.time_O41_R1, TimeData.time_O41_R2, TimeData.time_O41_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_H3, TimeData.time_O42_H3, TimeData.time_O42_H3, TimeData.time_O42_R1, TimeData.time_O42_R2, TimeData.time_O42_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, 9999, TimeData.time_O51_H2, 9999, 9999, TimeData.time_O51_H3, 9999, 9999, TimeData.time_O51_H3, 9999, 9999, TimeData.time_O51_H3, 9999, 9999],
    ]

    Time_H5R4 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_H3, TimeData.time_O11_H3, TimeData.time_O11_H3, TimeData.time_O11_R1, TimeData.time_O11_R2, TimeData.time_O11_R3, TimeData.time_O11_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_H3, TimeData.time_O12_H3, TimeData.time_O12_H3, TimeData.time_O12_R1, TimeData.time_O12_R2, TimeData.time_O12_R3, TimeData.time_O12_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_H3, TimeData.time_O13_H3, TimeData.time_O13_H3, TimeData.time_O13_R1, TimeData.time_O13_R2, TimeData.time_O13_R3, TimeData.time_O13_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_H3, TimeData.time_O21_H3, TimeData.time_O21_H3, TimeData.time_O21_R1, TimeData.time_O21_R2, TimeData.time_O21_R3, TimeData.time_O21_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_H3, TimeData.time_O22_H3, TimeData.time_O22_H3, TimeData.time_O22_R1, TimeData.time_O22_R2, TimeData.time_O22_R3, TimeData.time_O22_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_H3, TimeData.time_O23_H3, TimeData.time_O23_H3, TimeData.time_O23_R1, TimeData.time_O23_R2, TimeData.time_O23_R3, TimeData.time_O23_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_H3, TimeData.time_O31_H3, TimeData.time_O31_H3, TimeData.time_O31_R1, TimeData.time_O31_R2, TimeData.time_O31_R3, TimeData.time_O31_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_H3, TimeData.time_O32_H3, TimeData.time_O32_H3, TimeData.time_O32_R1, TimeData.time_O32_R2, TimeData.time_O32_R3, TimeData.time_O32_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_H3, TimeData.time_O41_H3, TimeData.time_O41_H3, TimeData.time_O41_R1, TimeData.time_O41_R2, TimeData.time_O41_R3, TimeData.time_O41_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_H3, TimeData.time_O42_H3, TimeData.time_O42_H3, TimeData.time_O42_R1, TimeData.time_O42_R2, TimeData.time_O42_R3, TimeData.time_O42_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, 9999, 9999, TimeData.time_O51_H2, 9999, 9999, 9999, TimeData.time_O51_H3, 9999, 9999, 9999, TimeData.time_O51_H3, 9999, 9999, 9999, TimeData.time_O51_H3, 9999, 9999, 9999],
    ]

    Time_H5R5 = [
        [TimeData.time_O11_H1, TimeData.time_O11_H2, TimeData.time_O11_H3, TimeData.time_O11_H3, TimeData.time_O11_H3, TimeData.time_O11_R1, TimeData.time_O11_R2, TimeData.time_O11_R3, TimeData.time_O11_R3, TimeData.time_O11_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O12_H1, TimeData.time_O12_H2, TimeData.time_O12_H3, TimeData.time_O12_H3, TimeData.time_O12_H3, TimeData.time_O12_R1, TimeData.time_O12_R2, TimeData.time_O12_R3, TimeData.time_O12_R3, TimeData.time_O12_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O13_H1, TimeData.time_O13_H2, TimeData.time_O13_H3, TimeData.time_O13_H3, TimeData.time_O13_H3, TimeData.time_O13_R1, TimeData.time_O13_R2, TimeData.time_O13_R3, TimeData.time_O13_R3, TimeData.time_O13_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O21_H1, TimeData.time_O21_H2, TimeData.time_O21_H3, TimeData.time_O21_H3, TimeData.time_O21_H3, TimeData.time_O21_R1, TimeData.time_O21_R2, TimeData.time_O21_R3, TimeData.time_O21_R3, TimeData.time_O21_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O22_H1, TimeData.time_O22_H2, TimeData.time_O22_H3, TimeData.time_O22_H3, TimeData.time_O22_H3, TimeData.time_O22_R1, TimeData.time_O22_R2, TimeData.time_O22_R3, TimeData.time_O22_R3, TimeData.time_O22_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O23_H1, TimeData.time_O23_H2, TimeData.time_O23_H3, TimeData.time_O23_H3, TimeData.time_O23_H3, TimeData.time_O23_R1, TimeData.time_O23_R2, TimeData.time_O23_R3, TimeData.time_O23_R3, TimeData.time_O23_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O31_H1, TimeData.time_O31_H2, TimeData.time_O31_H3, TimeData.time_O31_H3, TimeData.time_O31_H3, TimeData.time_O31_R1, TimeData.time_O31_R2, TimeData.time_O31_R3, TimeData.time_O31_R3, TimeData.time_O31_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O32_H1, TimeData.time_O32_H2, TimeData.time_O32_H3, TimeData.time_O32_H3, TimeData.time_O32_H3, TimeData.time_O32_R1, TimeData.time_O32_R2, TimeData.time_O32_R3, TimeData.time_O32_R3, TimeData.time_O32_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O41_H1, TimeData.time_O41_H2, TimeData.time_O41_H3, TimeData.time_O41_H3, TimeData.time_O41_H3, TimeData.time_O41_R1, TimeData.time_O41_R2, TimeData.time_O41_R3, TimeData.time_O41_R3, TimeData.time_O41_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
        [TimeData.time_O42_H1, TimeData.time_O42_H2, TimeData.time_O42_H3, TimeData.time_O42_H3, TimeData.time_O42_H3, TimeData.time_O42_R1, TimeData.time_O42_R2, TimeData.time_O42_R3, TimeData.time_O42_R3, TimeData.time_O42_R3, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],

        [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, TimeData.time_O51_H1, 9999, 9999, 9999, 9999, TimeData.time_O51_H2, 9999, 9999, 9999, 9999, TimeData.time_O51_H3, 9999, 9999, 9999, 9999, TimeData.time_O51_H3, 9999, 9999, 9999, 9999, TimeData.time_O51_H3, 9999, 9999, 9999, 9999],
    ]

TIME_TABLE_FUZZY =  TIME_TABLE()