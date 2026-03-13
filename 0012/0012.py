calculating = True

TARGET = 500

tri_nums : [int] = []
tri_num : int
counter = 2

def get_divisors(num : int) -> [int]:
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

while calculating:
    number = 0
    for i in range(1, counter):
        number += i
    tri_nums.append(number)
    divisors = get_divisors(number)
    if len(divisors) > TARGET:
        tri_num = number
        calculating = False
    counter += 1

print("The first triangle number with more then %d divisors is: %d"%(TARGET, number))
