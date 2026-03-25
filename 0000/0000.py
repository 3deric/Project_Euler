import time

TARGET = 691000

def calc_squares(target: int) -> list[int]:
    result : list[int] = []
    i = 0
    while len(result) <= target:
        result.append(i * i)
        i += 1

    return result

def sum_odd(numbers : list[int]) -> int:
    sum = 0
    for number in numbers:
        if number %2 != 0:
            sum += number

    return sum

if __name__ == '__main__':
    start_time = time.time()

    squares = calc_squares(TARGET)

    sum = sum_odd(squares)

    end_time = time.time()

    print("The sum of all odd squares in the first %d square numbers is: %d" % (TARGET, sum))
    print("Calculation took: %f seconds" % (end_time - start_time))