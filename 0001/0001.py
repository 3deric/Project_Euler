target : int = 1000
sum : int = 0

for i in range(0, target):
    if (i%3 == 0 or i%5 == 0):
        sum += i

print("The sum of multiples of 3 or 5 below %d is: %d" % (target, sum))