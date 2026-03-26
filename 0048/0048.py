import time

def self_powers(limit : int) -> int:
    result = 0
    for i in range(1, limit + 1):
        result += i ** i
    return result

if __name__ == '__main__':
    start_time = time.time()

    sum = self_powers(1000)

    end_time = time.time()

    digits = str(sum)[-10:]

    print("The last ten digits are %s" % (digits))
    print("Calculation took: %f seconds" % (end_time - start_time))

