RANGE : int = 100

sum_of_squares : int = 0
sum_squared : int = 0

if __name__ == '__main__':
    for i in range(1, RANGE + 1):
        sum_of_squares += (i * i)
    sum_squared = RANGE * (RANGE + 1) // 2
    sum_squared *= sum_squared

    print("The sum of squares is: %d." % sum_of_squares)
    print("The square of the sums is: %d." % sum_squared)
    print("The difference of both is: %d." % (sum_squared - sum_of_squares))