
def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

print("Are 'listen' and 'silent' anagrams?", is_anagram("listen", "silent"))
print("Are 'python' and 'java' anagrams?", is_anagram("python", "java"))
