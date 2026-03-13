import math

TARGET = 10001

primes : [int] = []

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    i : int = 0
    while len(primes) < TARGET:
        if is_prime(i):
            primes.append(i)
        i += 1
    print(primes)
    print("The %d. prime number is %d" %(TARGET, primes[-1]))