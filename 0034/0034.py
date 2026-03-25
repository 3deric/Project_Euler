import time

def factorial(n: int) -> int:
    result = 1
    for i in range(1,n + 1):
        result *= i
    return result

def is_factorial_sum(n : int) -> bool:
    digits = list(str(n))
    sum = 0
    for d in digits:
        sum += factorial(int(d))
    return n == sum

if __name__ == '__main__':
    start_time = time.time()

    sum = 0

    for i in range(3, 100000):
        if is_factorial_sum(i):
            sum += i

    end_time = time.time()

    print("The sum of all numbers which are equal to the sum of their factorial digits is: %d" % sum)
    print("Calculation took: %f seconds" % (end_time - start_time))

