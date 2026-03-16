triangle = []

def max_path_sum(triangle : []) ->  int:
    while len(triangle) > 0:
        if len(triangle) > 1:
            for index in range(0,len(triangle[-2])):
                triangle[-2][index] += max(triangle[-1][index:index+2])
        else:
            return triangle[0][0]
        del triangle[-1]

with open('0067_triangle.txt', 'r') as file:
    for line in file:
        int_row = []
        row = line.split()
        for char in row:
            int_value = int(char)
            int_row.append(int_value)
        triangle.append(int_row)

print("The maximum path sum is %d" % max_path_sum(triangle))