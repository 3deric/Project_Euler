num = 100

def factorial(num : int) -> int:
    fac = 1
    while num > 0:
        fac *= num
        num -= 1
    return fac

def sum_digits(num : int) -> int:
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

factorial = factorial(num)
factorial_sum = sum_digits(factorial)

print("The factorial digit sum of %d! is: %d" % (num, factorial_sum))