import re


def is_valid_email(email):
    pattern = r'^[A-Za-z0-9._+]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$'
    if not re.match(pattern,email):
        return False
    username = email.split('@')[0]
    if '..' in username:
        return False
    return True

def test_email_valid(): 
    assert is_valid_email("user.name+1@gmail.com") 
    assert is_valid_email("test_user@domain.co.in") 

def test_email_invalid(): 
    assert not is_valid_email("user..name@gmail.com") 
    assert not is_valid_email("user@domain") 
    assert not is_valid_email("@domain.com")