from regex_utils import is_valid_email,is_valid_phone


def test_email():
    assert is_valid_email("seshaiahvanka@gmail.com")
    assert not is_valid_email("bad-email")

def test_phone():
    assert is_valid_phone("9888949430")
    assert not is_valid_phone("143363")