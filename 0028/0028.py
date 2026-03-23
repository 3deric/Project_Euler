LEN = 1001

# initialize a 2d grid with zeros
# walk through the 2d grid, starting at the center
# always 2 times the same step width, then step with gets increased
# step width increases by 1 every 2 direction changes
# direction change happens after steps in a direction have been finished
# stops when the upper right corner is reached

def fill_grid(len : int) -> []:
    grid =  [ [ 0 for i in range(len) ] for j in range(len) ]
    i = 1
    dir = 0
    # 0 = right
    # 1 = down
    # 2 = left
    # 3 = up
    steps = 1
    pos = (len//2, len//2)
    while i <= len*len:
        for s in range(steps):
            grid[pos[0]][pos[1]] = i
            if dir == 0:
                pos = (pos[0] ,pos[1] +1)
            elif dir == 1:
                pos = (pos[0] +1 ,pos[1])
            elif dir == 2:
                pos = (pos[0],pos[1] -1)
            else:
                pos = (pos[0] -1 ,pos[1])
            i+=1
        dir = (dir + 1) % 4
        if dir % 2 == 0:
            steps += 1

    return grid

def draw_grid(grid : []) -> None:
    for i in grid:
        print(i)

def sum_diagonals(grid : []) -> int:
    sum = 0
    j = 0
    k = len(grid) - 1
    # sum diagonals from both directions
    for i in range(LEN):
        sum += grid[i][j]
        sum += grid[i][k]
        j += 1
        k -= 1
    # subtracting the centerpoint from the diagonals
    return sum -1

if __name__ == '__main__':
    grid = fill_grid(LEN)
    # draw_grid(grid)
    sum = sum_diagonals(grid)
    print("The sum of the diagonals in a %d by %d spiral is %d" % (len(grid), len(grid), sum))


