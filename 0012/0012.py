TARGET = 500

tri_num : int
i = 2
calculating = True
longest = 0
number = 0
next = 0

def get_divisors(num : int) -> [int]:
    divisors = []
    for i in range(1, int(num/2) + 1):
        if num % i == 0:
            divisors.append(i)
    divisors.append(num)
    return divisors

while calculating:
    next +=1
    number += next
    divisors = get_divisors(number)
    if len(divisors) > TARGET:
        tri_num = number
        calculating = False
    if len(divisors) > longest:
        longest = len(divisors)
    i += 1

print("The first triangle number with more then %d divisors is: %d"%(TARGET, number))
