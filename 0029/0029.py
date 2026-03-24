import time

from orca.braille import endIsShowing

RANGE_START = 2
RANGE_END = 101

def calculate_distinct_powers(start : int, end : int) -> list[int]:
    result : list[int] = []

    for i in range(start, end):
        for j in range(start, end):
            pow = i ** j
            if pow not in result:
                result.append(pow)
    return result


if __name__ == '__main__':
    start_time = time.time()

    powers = calculate_distinct_powers(RANGE_START, RANGE_END)

    end_time = time.time()

    print("There are %d distinct terms generated in the range between %d and %d" %(len(powers), RANGE_START, RANGE_END))
    print("Calculation took: %f seconds" %(end_time - start_time))