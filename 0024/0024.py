numbers1 : [int] = [0,1,2]
numbers2 : [int] = [0,1,2,3,4,5,6,7,8,9]
permutations = []

def swap(list : [], a : int, b : int) -> []:
    temp = list[a]
    list[a] = list[b]
    list[b] = temp
    return list

def permute(list: []):
    start = 0
    end = len(list)-1
    generate(list, start , end)

def generate(list, start, end):
    if start == end:
        global permutations
        permutations.append(list.copy())

    for i in range(start, end + 1):
        swap(list, start, i)
        generate(list, start + 1, end)
        swap(list, start, i)

def order_lexicographic(list : []) -> []:
    return list.sort()

permute(numbers2)

order_lexicographic(permutations)

print("The millionth permutation of 0,1,2,3,4,5,6,7,8,9 is:")
print(permutations[999999])