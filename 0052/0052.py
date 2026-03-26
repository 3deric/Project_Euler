import time

MULTIPLES = 6

def sort_digits(num : int) -> list[str]:
    result = sorted(list(str(num)))
    return result

def check_permuted_multiples(num : int, multiples : int) -> bool:
    compare = sort_digits(num)
    for i in range(1, multiples + 1):
        if compare != sort_digits(num * i):
            return False
    return True

if __name__ == '__main__':
    start_time = time.time()

    result = 1
    running = True

    while running:
        if check_permuted_multiples(result, MULTIPLES):
            running = False
            break
        result +=1

    end_time = time.time()

    print("The smallest possible integer is %d" % result)

    print("Calculation took: %f seconds" % (end_time - start_time))


