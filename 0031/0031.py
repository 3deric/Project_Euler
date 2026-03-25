import time

TARGET = 200

# totally absurd for loop

def coin_sum():
    result = 0
    for two_l in range(0,2):
        for one_l in range(0, 3 - 2 * two_l):
            for fifty_p in range(0,5 - 4 * two_l - 2 * one_l):
                for twenty_p in range(0,11 - 10 * two_l - 5 * one_l - 2 * fifty_p):
                    for ten_p in range(0,21 - 20 * two_l - 10 * one_l - 5 * fifty_p - 2 * twenty_p):
                        for five_p in range(0,41 - 40 * two_l - 20 * one_l - 8 * fifty_p - 4 * twenty_p - 2 * ten_p):
                            for two_p in range(0,101 - 100 * two_l - 50 * one_l - 25 * fifty_p - 10 * twenty_p - 5 * ten_p):
                                for one_p in range(0,201 - 200 * two_l - 100 * one_l - 50 * fifty_p - 20 * twenty_p - 10 * ten_p):
                                    sum = two_l * 200 + one_l * 100 + fifty_p * 50 + twenty_p * 20 + ten_p * 10 + five_p * 5 + two_p * 2 + one_p
                                    if sum > TARGET:
                                        break
                                    if sum == TARGET:
                                        result += 1
    return result

if __name__ == '__main__':
    start_time = time.time()

    variants = coin_sum()

    end_time = time.time()

    print("There are %d different ways £2 can be made using any number of coins" % variants)
    print("Calculation took: %f seconds" % (end_time - start_time))