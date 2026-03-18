# simple while loop, stops when the amount if digits is reached
# digits are counted by converting the last number to str
# if the string length is < Target new numbers are generated

def generate_fibonacci(target: int) -> []:
    result = [1,1]
    while len(str(result[-1])) < target:
        next = result[-1] + result[-2]
        result.append(next)
    return result

fibonacci = generate_fibonacci(1000)

print("The index of the first term in in the Fibonacci sequence with 1000 digits is: %d" % (len(fibonacci)-1))
