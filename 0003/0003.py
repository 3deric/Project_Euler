# Generate a list of primes til 1000
# then generate all prime factors for a defined number
# 140 = 2 * 70 #can be divided by 2, 70 is not prime
# 140 = 2 * 2 * 35 # can be divided by 2, 35 is not prime
# 140 = 2* 2* 5 * 7 # can be divided by 5, both numbers are prime

import math

target = 600851475143
primes : [int] = []

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def get_prime_factors(num : int) -> []:
    calc = True
    factors: [int] = []
    temp = num
    while calc:
        for p in primes:
            if temp == p:
                calc = False
            if temp % p == 0:
                factors.append(p)
                temp /= p
                continue

    return factors

def generate_primes(range_to : int) -> []:
    primes : [int] = []
    for i in range(range_to):
        if is_prime(i) == True:
            primes.append(i)
    return primes

def calculate_number_from_primes(factors : [int]) -> int:
    result = 1
    for p in factors:
        result *= p
    return result


if __name__ == '__main__':
    primes = generate_primes(10000)
    factors : [int] = get_prime_factors(target)
    print(factors)
    print("The highest prime factor of %d is: %d" %(target,max(factors)))





