palindrome : tuple()

# convert the number to a string and invert the string
# compare if both strings are the same
def is_palindrome(num) -> bool:
    return str(num) == str(num)[::-1]

if __name__ == '__main__':
    for i in range(100, 1000):
        for j in range(100,1000):
            temp = i * j
            if (is_palindrome(temp)):
                palindrome = (i, j, temp)

print("The largest palindrome of two 3-digit numbers is: %d." %(palindrome[2]))
print("The number is the product of %d and %d." %(palindrome[0], palindrome[1]))



