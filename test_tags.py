import re


def is_valid_tag(text):
    return re.findall(r'<\s*(\w+)',text)

def test_tag():
    text = "<div>Hello</div><p>World</p>"
    assert is_valid_tag(text) == ["div", "p"]