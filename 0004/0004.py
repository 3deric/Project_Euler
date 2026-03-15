palindrome : tuple() = (0,0,0)

# convert the number to a string and invert the string
# compare if both strings are the same
def is_palindrome(num) -> bool:
    return str(num) == str(num)[::-1]

if __name__ == '__main__':
    for i in range(1, 1000):
        for j in range(1,1000):
            temp = i * j
            if (is_palindrome(temp)):
                if temp > palindrome[2]:
                    palindrome = (i, j, temp)

print("The largest palindrome of two 3-digit numbers is: %d." %(palindrome[2]))
print("The number is the product of %d and %d." %(palindrome[0], palindrome[1]))



