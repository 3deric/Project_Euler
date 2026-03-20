import math

# solved with a tutorial by 'Good Morning Developers'
TARGET = 28123

abundant_numbers = []
factors = [1] * TARGET
# # create all abundant numbers below the threshold
for i in range(2, math.isqrt(TARGET)):
    for j in range(i, TARGET//i):
        if i == j:
            factors[i*j] += i
        else:
            factors[i*j] += i + j

# factors list contains the sum of all proper divisors of all number below the Target
print(factors[0:20])
# i is the number itself, for example 100
# num is the number of divisors
# of the number is bigger then i then its a abundant number
# zero needs to be removed from the list
for i, num in enumerate(factors):
    if num > i:
        abundant_numbers.append(i)
abundant_numbers.pop(0) # remove leading zero
print(abundant_numbers[0:20])

non_abundant_numbers = [num for num in range(TARGET)]

for i in range(len(abundant_numbers)):
    # outer loop, lower number
    for j in range(i, len(non_abundant_numbers)):
        # inner loop for the upper number
        lower_number = abundant_numbers[i]
        upper_number = abundant_numbers[j]
        sum_of_numbers = lower_number + upper_number
        if sum_of_numbers < TARGET:
            non_abundant_numbers[sum_of_numbers] = 0
        else:
            break
            
print("The sum of all positive integers which cannot be written\nby the sum of two abundant numbers is: %d" % sum(non_abundant_numbers))