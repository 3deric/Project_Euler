import time

TARGET = 1000000

def is_palindrome(num) -> bool:
    return str(num) == str(num)[::-1]

if __name__ == '__main__':
    start_time = time.time()

    sum = 0

    for i in range(0, TARGET):
        if is_palindrome(i) and is_palindrome(int(bin(i)[2:])):
            sum += i

    end_time = time.time()

    print("The sum of all palindromic numbers in either base less then one million is: %d" % sum)
    print("Calculation took: %f seconds" % (end_time - start_time))



