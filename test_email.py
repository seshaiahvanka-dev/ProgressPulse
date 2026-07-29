import re


def is_valid_email(text):
    return re.findall(r'[A-Za-z0-9._+]+@[A-Za-z0-9._]+\.[A-Za-z]{2,6}',text)

def test_email():
    text = "Contact us at info@example.com or support@test.org"
    assert is_valid_email(text) == ["info@example.com", "support@test.org"]