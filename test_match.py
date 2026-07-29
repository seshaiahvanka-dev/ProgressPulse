import re


def is_match_words(text):
    return re.findall(r'Py[A-Za-z]+',text)

def test_match():
    text = "Python, PyCharm, Pygame, Ruby, Java"
    assert is_match_words(text) == ["Python", "PyCharm", "Pygame"]
