TARGET = 1000

# number lists from stackoverflow
ones = ['', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty',
        'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

numbers = []
letters = 0

def num_as_words(num : int) -> str:
    string = ""
    if num >= 1000 and num < 10000:
        thou = num // 1000
        num -= thou * 1000
        string += ones[thou] + ' thousand '
    if num >= 100 and num < 1000:
        hun = num // 100
        num -= hun * 100
        string += ones[hun] + ' hundred'
        if num > 0:
            string += ' and'
    if num >= 20 and num < 100:
        ten = num // 10
        num -= ten * 10
        string += ' ' + tens[ten]
    if num < 20:
        string += ' ' + ones[num]

    return string

for i in range(1,TARGET+1):
    to_words = num_as_words(i)
    numbers.append(to_words)
    letters += len(to_words.strip())

print("All numbers from 1 to %d written out use %d letters" %(TARGET, letters))

for i in range(0,TARGET):
    print(numbers[i])