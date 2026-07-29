import re


def is_valid_date(text):
    return re.findall(r'\d{2}-\d{2}-\d{4}',text)

def test_date():
    text = "Today is 10-07-2026, yesterday was 09-07-2026"
    assert is_valid_date(text) == ["10-07-2026", "09-07-2026"]