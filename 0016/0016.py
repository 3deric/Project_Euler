num = 1000

# get the last digit by performing a modulo 10, remainder is the last digit
# remainder gets added to the sum
# perform a integer division to remove the last digit from the number
# perform til number is 0

def power_digit_sum(num : int) -> int:
    num = 2 ** num
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

print("The som of the digits of 2^%d is: %d" %(num,power_digit_sum(num)))