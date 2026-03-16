TARGET = 1000000
longest : tuple = (0,0)

def get_next_collatz(num: int) -> int:
    if num % 2 == 0:
        return num // 2
    return 3 * num + 1

for i in range(1,TARGET):
    start_num = i
    num = i
    sequence = []
    while True:
        num = get_next_collatz(num)
        sequence.append(num)
        if num == 1:
            if len(sequence) > longest[1]:
                longest = (start_num, len(sequence))
            break

print("The starting number %d under %d produces the longest chain with %d entries" %(longest[0],TARGET,longest[1]))
