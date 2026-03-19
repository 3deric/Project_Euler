def calculate_decimals(div : int) -> []:
    num = 1
    result = []
    while len(result) < 25:
        next = num * 10 // div
        result.append(next)
        num =  num * 10 - (next * div)
        cycle = check_cycle(result)
        if cycle[0]:
            print(cycle[1])
    return result

def check_cycle(result : list[int]) -> tuple():
    if len(result) < 2 or len(result) % 2 != 0:
        return (False, [])
    mid = len(result) // 2
    x = result[:mid]
    y = result[mid:]
    if sum(y) // len(y) == y[0]:
        return (True, y[0])
    if x == y:
        return (True, y)
    return (False, y)

calculate_decimals(7)
#divide
#multiply back
#subtract
#repeat til remainder is 0, or repeats infinite


# 10 : 6 = 166
#  6
#  40
#  36
#   40
#   36