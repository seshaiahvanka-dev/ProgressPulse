
def is_palindrome(word):
    return word == word[::-1]

print("Is 'madam' a palindrome?", is_palindrome("madam"))
print("Is 'python' a palindrome?", is_palindrome("python"))
