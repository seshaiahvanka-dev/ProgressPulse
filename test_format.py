import re


def is_valid_ing(text):
    return re.findall(r'[A-Za-z]{3,}ing',text)

def test_format():
    text = "running, walking, sing, ring, king"
    assert is_valid_ing(text) == ["running", "walking"]