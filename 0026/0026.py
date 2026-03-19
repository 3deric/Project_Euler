def calculate_decimals(div : int) -> []:
    num = 1
    result = []
    while len(result) < 1000:
        prev = num * 10
        next = prev // div
        result.append(next)
        num = prev - next * div
    return result

print(calculate_decimals(7))
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