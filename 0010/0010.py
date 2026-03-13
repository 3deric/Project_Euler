import math

TARGET = 2000000

primes : [int] = []

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

for i in range(2, TARGET):
    if is_prime(i):
        primes.append(i)

print("The sum of all primes below two million is: %d"%(sum(primes)))