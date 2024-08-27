import os

combinations = [
    # pop_size, p_crossover, p_mutation, tSize, p_cross_machine, p_mutation_machine, max_iteration
    [200, 0.5, 0.1, 4, 0.16, 0.16, 1000],
    [200, 0.6, 0.2, 5, 0.33, 0.33, 1000],
    [200, 0.7, 0.3, 6, 0.50, 0.50, 1000],
    [200, 0.8, 0.4, 7, 0.67, 0.67, 1000],
    [200, 0.9, 0.5, 8, 0.83, 0.83, 1000],
    [250, 0.5, 0.3, 8, 0.33, 0.67, 1000],
    [250, 0.6, 0.4, 4, 0.50, 0.83, 1000],
    [250, 0.7, 0.5, 5, 0.67, 0.16, 1000],
    [250, 0.8, 0.1, 6, 0.83, 0.33, 1000],
    [250, 0.9, 0.2, 7, 0.16, 0.50, 1000],
    [300, 0.5, 0.5, 7, 0.50, 0.33, 1000],
    [300, 0.6, 0.1, 8, 0.67, 0.50, 1000],
    [300, 0.7, 0.2, 4, 0.83, 0.67, 1000],
    [300, 0.8, 0.3, 5, 0.16, 0.83, 1000],
    [300, 0.9, 0.4, 6, 0.33, 0.16, 1000],
    [350, 0.5, 0.2, 6, 0.67, 0.83, 1000],
    [350, 0.6, 0.3, 7, 0.83, 0.16, 1000],
    [350, 0.7, 0.4, 8, 0.16, 0.33, 1000],
    [350, 0.8, 0.5, 4, 0.33, 0.50, 1000],
    [350, 0.9, 0.1, 5, 0.50, 0.67, 1000],
    [400, 0.5, 0.4, 5, 0.83, 0.50, 1000],
    [400, 0.6, 0.5, 6, 0.16, 0.67, 1000],
    [400, 0.7, 0.1, 7, 0.33, 0.83, 1000],
    [400, 0.8, 0.2, 8, 0.50, 0.16, 1000],
    [400, 0.9, 0.3, 4, 0.67, 0.33, 1000],
]

path = "D:\\python\\optimal\\orthogonalTest\\results\\H3R3P3\\5\\"
output = ""

for pop_size, p_crossover, p_mutation, tSize, p_cross_machine, p_mutation_machine, max_iteration in combinations:
    name = "popSize={}_pCrossover={}_pCrossMS={}_pMutate={}_pMutateMS={}_maxIteration={}.xlsx".format(pop_size, p_crossover, p_cross_machine, p_mutation, p_mutation_machine, max_iteration)
    find = False
    for file_name in os.listdir(path):
        if name in file_name:
            output += file_name[:3] + " "
            find = True
    if not find:
        output += "NONE" + " "
print(output)