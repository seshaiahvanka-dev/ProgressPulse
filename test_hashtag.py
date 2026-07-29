import re


def is_hashtag(text):
    return re.findall(r'#\w+',text)

def test_tags():
    text = "Loving #regex practice! #Python #Coding"
    assert is_hashtag(text) == ["#regex", "#Python", "#Coding"]