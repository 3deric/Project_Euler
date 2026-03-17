TARGET = 10000

numbers = []

def is_amicable(m : int) -> bool:
    n = sum(get_divisors(m))
    return m != n and m == sum(get_divisors(n))

def get_divisors(number: int) -> [int]:
    divisors = []
    for divisor in range(1, number // 2 + 1):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors

for i in range(1, TARGET):
    if is_amicable(i):
        numbers.append(i)

print(numbers)

print("\nThe sum of all amicable numbers under %d is: %d" % (TARGET, sum(numbers)))
