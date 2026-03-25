import time

POWER = 5

# First generate a list of numbers to define the upper limit
# loop from 2 to the upper limit, starting at the first sum 2
# split the number into its digits
# loop over every digit
# add the power of every digit to a temp sum
# if sum exceeds the current loop iteration -> break
# if the sum is equal the current iteration -> append

def set_upper_limit(power) -> int:
    result = 0
    for i in range(0,power):
        result += 9 ** power
    return result

def digit_powers(power : int) -> list[int]:
    limit = set_upper_limit(power)
    result = []
    for i in range(2, limit):
        sum = 0
        digits = list(str(i))
        for d in digits:
            d = int(d)
            sum += pow(d, power)
            if sum > i:
                break
        if sum == i:
            result.append(i)
    return result

if __name__ == '__main__':
    start_time = time.time()

    sum = 0

    print(digit_powers(POWER))

    end_time = time.time()

    print("Calculation took: %f seconds" % (end_time - start_time))