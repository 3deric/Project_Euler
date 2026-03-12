RANGE_START : int = 1
RANGE_END : int = 20

# perform a modulo operation to check if a remainder exists
# early return if a remainder is found

def no_remainder_in_range(num : int) -> bool:
    for i in range(RANGE_START,RANGE_END):
        if num % i != 0:
            return False
    return True

if __name__ == '__main__':
    calculate = True
    num = 1
    while calculate:
        if(no_remainder_in_range(num)):
            break
        num += 1

    print("The smallest number without any remainder in the range %d to %d is: %d."%(RANGE_START,RANGE_END,num))
