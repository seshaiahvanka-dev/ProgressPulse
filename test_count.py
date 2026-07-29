import re


def is_five(text):
    return re.findall(r'[A-Za-z]{5}',text)

def test_five():
    text = "apple, mango, pear, grapes, berry" 
    assert is_five(text) == ["apple", "mango", "grape", "berry"]