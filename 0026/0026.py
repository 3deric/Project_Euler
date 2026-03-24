import time

TARGET = 1000

start_time = time.time()

# calculate the decimals by performing a simple manual division
# store remainder of calculation in a set
# if the remainder occurs again -> cycle repeats
# prime numbers have a reciprocal cycle which is num -1, this could be another solution

def calculate_decimals(div : int) -> list[int]:
    num = 1
    result = []
    remainders : set = set()
    while True:
        # calculate remainder
        remainder = num % div
        if remainder in remainders:
            break
        remainders.add(remainder)
        # calculate next decimal
        next = num * 10 // div
        result.append(next)
        # calculate next base number
        num =  num * 10 - (next * div)
    return result

longest : tuple = (0,0, [])

for i in range(2, TARGET):
    dec = calculate_decimals(i)
    # print(len(dec), dec)
    if longest[1] < len(dec):
        longest = (i, len(dec), dec)

end_time = time.time()

print(longest[2])
print("The number under 1/%d with %d reciprocal decimals is %d\n" %(TARGET, longest[1], longest[0]))
print("It took %f seconds to calculate" %(end_time - start_time))
