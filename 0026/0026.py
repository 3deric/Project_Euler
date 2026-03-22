import time

TARGET = 1000
MAX_DECIMALS = 1000

# calculate the decimals by performing a simple manual division
# check for the remainder of the first calculation, save it!
# if the remainder appears again, break from the loop
# the result ist the cycle

def calculate_decimals(div : int) -> tuple():
    num = 1
    result = []
    decimals_cycle = []
    #while len(result) < MAX_DECIMALS:
    while True:
        # calculate next decimal
        next = num * 10 // div

        result.append(next)
        # calculate next base number
        num =  num * 10 - (next * div)
        cycle = get_reciprocal_cycles(result)
        if cycle:
            decimals_cycle = cycle
            break
    return decimals_cycle


def get_reciprocal_cycles(decimals : list[int]) -> list[int]:
    cycle = []

    if len(decimals) < 2:
        return
    if sum(decimals)  == 0:
        return [0]
    while decimals[0] == 0:
        del decimals[0]
    for i in range(2, len(decimals) + 1, 2):
        test_decimals = decimals[-i:]
        h1 = test_decimals[len(test_decimals)//2:]
        h2 = test_decimals[:len(test_decimals) // 2]
        #print(h1,h2)
        if h1 == h2:
            cycle = h1
            break
    return cycle

start_time = time.time()

longest : tuple = (0,[])

for i in range(2, TARGET):
    current = calculate_decimals(i)
    print(i, current)
    #print(current)
    #if current[0] == True and len(current[1]) > len(longest[1]):
    #    longest = (i, current[1])

end_time = time.time()
#print(longest)
#print("Time Taken:", end_time - start_time)

# 10 : 6 = 16      # remainder 4 on first calculation
#  6                # remainder 4 on second calculation too
#  40               # remainder defines the start and end of the looping area

# 10 : 4 = 25
#  8    decimals_h2 = decimals[half:]
#  20
#  20
#   0