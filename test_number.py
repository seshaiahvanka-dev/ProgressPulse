import re


def is_valid_num(text):
    return re.findall(r'\d+',text)

def test_num():
    text = "Order123, Item45, Price=99"
    assert is_valid_num(text) == ["123", "45", "99"]