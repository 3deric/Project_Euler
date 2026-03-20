TARGET = 10
MAX_DECIMALS = 10

# calculate the decimals by performing a simple manual division
# check for the remainder of the first calculation, save it!
# if the remainder appears again, break from the loop
# the result ist the cycle

# print(10 // 4)
# print((10 // 4 * 4))
# print(10 - 8)
# print(2 * 10 // 4)

def calculate_decimals(div : int) -> list[int]:
    num = 1
    result = []
    first_remainder = -1
    remainders = []

    while len(result) < MAX_DECIMALS:
        # calculate the remainder of the division
        remainder = num * 10 % div

        # calculate next decimal
        next = num * 10 // div
        result.append(next)

        # calculate next base number
        num =  num * 10 - (next * div)
        if len(remainders) > 0:
            pass
        remainders.append(remainder)

    return result

# 10 : 6 = 16      # remainder 4 on first calculation
#  6                # remainder 4 on second calculation too
#  40               # remainder defines the start and end of the looping area

# 10 : 4 = 25
#  8
#  20
#  20
#   0
#for i in range(2, TARGET):
#    print(i, calculate_decimals(i))

print(calculate_decimals(7))
