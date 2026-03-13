MAX_RANGE = 10000
TARGET = 10000

# iterate over the range in a 2 dimensional for loop
# start of the second for loop must be higher then the current iteration
# calculate c by subtracting a and b from 1000
# check if a² + b² = c²
for a in range(1,MAX_RANGE + 1):
    for b in range(a + 1,MAX_RANGE +1):
        c = 1000 - a - b
        if c < 0:
            continue
        if a * a + b * b == c * c:
            print("The numbers are a=%d, b=%d, c=%d." % (a,b,c))
            break