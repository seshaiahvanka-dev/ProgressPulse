
def word_frequency(text):
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

sample_text = "python is fun and python is powerful"
print("Word frequencies:", word_frequency(sample_text))
