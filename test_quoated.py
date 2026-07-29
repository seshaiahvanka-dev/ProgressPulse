import re


def is_quoated(text):
    return re.findall(r'"([^"]+)"',text)

def test_quoate():
    text = 'He said, "Hello World" and left.'
    assert is_quoated(text) == ['Hello World']