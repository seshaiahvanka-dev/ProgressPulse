import re


def is_valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$",email) is not None

def is_valid_phone(phone):
    return re.match(r"^\d{10}$",phone) is not None