# not my own solution
TARGET = 20

def count_paths(grid_size):
    # init 2d list with ones
    paths = [[1] * (grid_size + 1)] * (grid_size + 1)
    for i in range(1, grid_size + 1):
        for j in range(1, grid_size + 1):
            paths[i][j] = paths[i-1][j] + paths[i][j-1]
    return paths[grid_size][grid_size]

print("There are %d routes in a %d by %d grid" %(count_paths(TARGET), TARGET, TARGET))