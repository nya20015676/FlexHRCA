import os
import pandas as pd

path_list = ["/home/amtc/Desktop/optimal/comparison/CSP/H1/H1R1/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H1/H1R2/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H1/H1R3/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H1/H1R4/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H1/H1R5/",
            
             "/home/amtc/Desktop/optimal/comparison/CSP/H2/H2R1/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H2/H2R2/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H2/H2R3/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H2/H2R4/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H2/H2R5/",

             "/home/amtc/Desktop/optimal/comparison/CSP/H3/H3R1/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H3/H3R2/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H3/H3R3/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H3/H3R4/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H3/H3R5/",

             "/home/amtc/Desktop/optimal/comparison/CSP/H4/H4R1/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H4/H4R2/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H4/H4R3/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H4/H4R4/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H4/H4R5/",

             "/home/amtc/Desktop/optimal/comparison/CSP/H5/H5R1/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H5/H5R2/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H5/H5R3/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H5/H5R4/",
             "/home/amtc/Desktop/optimal/comparison/CSP/H5/H5R5/",

             "/home/amtc/Desktop/optimal/comparison/SVTN/H1/H1R1/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H1/H1R2/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H1/H1R3/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H1/H1R4/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H1/H1R5/",

             "/home/amtc/Desktop/optimal/comparison/SVTN/H2/H2R1/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H2/H2R2/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H2/H2R3/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H2/H2R4/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H2/H2R5/",

             "/home/amtc/Desktop/optimal/comparison/SVTN/H3/H3R1/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H3/H3R2/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H3/H3R3/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H3/H3R4/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H3/H3R5/",

             "/home/amtc/Desktop/optimal/comparison/SVTN/H4/H4R1/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H4/H4R2/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H4/H4R3/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H4/H4R4/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H4/H4R5/",

             "/home/amtc/Desktop/optimal/comparison/SVTN/H5/H5R1/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H5/H5R2/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H5/H5R3/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H5/H5R4/",
             "/home/amtc/Desktop/optimal/comparison/SVTN/H5/H5R5/",

             
             "/home/amtc/Desktop/optimal/comparison/TFN/H1/H1R1/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H1/H1R2/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H1/H1R3/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H1/H1R4/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H1/H1R5/",
             
             "/home/amtc/Desktop/optimal/comparison/TFN/H2/H2R1/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H2/H2R2/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H2/H2R3/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H2/H2R4/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H2/H2R5/",
             
             "/home/amtc/Desktop/optimal/comparison/TFN/H3/H3R1/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H3/H3R2/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H3/H3R3/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H3/H3R4/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H3/H3R5/",
             
             "/home/amtc/Desktop/optimal/comparison/TFN/H4/H4R1/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H4/H4R2/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H4/H4R3/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H4/H4R4/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H4/H4R5/",
             
             "/home/amtc/Desktop/optimal/comparison/TFN/H5/H5R1/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H5/H5R2/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H5/H5R3/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H5/H5R4/",
             "/home/amtc/Desktop/optimal/comparison/TFN/H5/H5R5/",]

for directory in path_list:

    # Get a list of all Excel files in the directory
    excel_files = [file for file in os.listdir(directory) if (file.endswith('.xlsx') and not "testdata" in file)]
    if excel_files != []:
        sorted_files = sorted(excel_files, key=lambda x: int(x[x.find("-") + 1:x.find(".")]))

        total = 0
        # Iterate over each Excel file
        min_file = sorted_files[0]
        min_file_path = os.path.join(directory, min_file)
        
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(min_file_path)
        
        # Find the last occurrence of '1' in the 'Optimal Size' column
        last_row_with_one = df[df['Optimal Size'] == 1].index[-1]
        total += last_row_with_one

        # Find the test results
        with open(directory+'result.txt', 'r') as file:
            # Iterate through each line in the file
            for line in file:
                # Check if the line starts with
                    # Split the line by spaces
                columns = line.split()
                if min_file[0:2].replace('-','') == columns[0].replace('-',''):
                    # Extract the second column (index 1)
                    avg = columns[1]
                    dev = columns[2]
                    range = columns[3]
                    max = columns[4]
                    min = columns[5]
                    break
        
        print("{} iterations to optimal {:.2f} fitness {} avg {} dev {} range {} max {} min {}".format(directory, total, min_file[min_file.find("-") + 1:min_file.find(".")], avg, dev, range, max, min))