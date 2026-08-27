
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print("Number of vowels in 'Seshu Vanka' is:", count_vowels("Seshu Vanka"))
