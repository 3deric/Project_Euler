import time

TARGET = 100
MAX_DECIMALS = 50
MIN_CYCLE_CHECK_LEN = 10

start_time = time.time()

# calculate the decimals by performing a simple manual division
# check for the remainder of the first calculation, save it!
# if the remainder appears again, break from the loop
# the result ist the cycle

def calculate_decimals(div : int) -> tuple():
    num = 1
    result = []
    decimals_cycle = []
    first_remainder = -1
    while len(result) < MAX_DECIMALS:
    #while True:
        # calculate next decimal
        remainder = num * 10 % div
        next = num * 10 // div
        print(remainder, next)
        result.append(next)
        # calculate next base number
        num =  num * 10 - (next * div)
        cycle = get_reciprocal_cycles(result)
    return (result, cycle)


def get_reciprocal_cycles(decimals : list[int]) -> list[int]:
    cycle = []
    for i in range(2, len(decimals) + 1, 2):
        test_decimals = decimals[-i:]
        h1 = test_decimals[len(test_decimals)//2:]
        h2 = test_decimals[:len(test_decimals) // 2]
        if h1 == h2:
            cycle = h1
            print(h1, h2)
            #print(cycle)
            break
    return cycle

longest : tuple = (0,0, [])

for i in range(2,10):
    calculate_decimals(i)

# for i in range(2, TARGET):
#      current = calculate_decimals(i)
#      print(i, len(current[1]), current)
#      if longest[1] < len(current[1]):
#          longest = (i, len(current[1]), current[0][:10])

end_time = time.time()

print("The number under 1/%d with %d reciprocal decimals is %d\n" %(TARGET, longest[1], longest[0]))
print("It took %f seconds to calculate" %(end_time - start_time))