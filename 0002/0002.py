target : int = 4000000
a : int = 1
b : int = 2
sum : int = 0

while b <= target:
    if b % 2 == 0:
        sum += b
    temp : int = b
    b += a
    a = temp

print("The sum of all even Fibonacci Numbers below %d is: %d\n" %(target, sum))