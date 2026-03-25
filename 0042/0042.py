import time


def is_triangle_word(word : str, triangle_numbers : list[int]) -> bool:
    letters = list(word.lower())
    sum = 0
    for l in letters:
        sum += (ord(l)- 96)
    return sum in triangle_numbers

def generate_triangle_numbers(word: str) -> list[int]:
    result :list[int] = [1]
    threshold = int(sum_word_letters(word)) * 2
    i = 2
    while result[-1] < threshold:
        result.append(int(1/2 * i * (i + 1)))
        i += 1

    return result

def sum_word_letters(word: str) -> int:
    sum = 0
    letters = list(word.lower())
    for l in letters:
        sum += ord(l) - 96
    return sum

if __name__ == '__main__':
    start_time = time.time()

    words = []

    with open('0042_words.txt') as f:
        words_input = f.read().replace('"', '').split(",")
        words = sorted(words_input, key=len)

    triangle_numbers = generate_triangle_numbers(words[-1])

    sum = 0
    for word in words:
        if is_triangle_word(word, triangle_numbers):
            sum += 1

    end_time = time.time()

    print("There are %d triangle words in the file" % (sum))
    print("Calculation took: %f seconds" % (end_time - start_time))


