import pytest
from user_registration import UserRegistration

list_of_emails = [("abc@yahoo.com", True), ("abc-100@yahoo.com", True), ("abc.100@yahoo.com", True),
                  ("abc111@abc.com", True), ("abc-100@abc.net", True), ("abc.100@abc.com.au", True),
                  ("abc@1.com", True),
                  ("abc@gmail.com.com", True), ("abc+100@gmail.com", True), ("abc", False), ("abc@.com.my", False),
                  ("abc123@gmail.a", False),
                  ("abc123@.com", False), ("abc123@.com.com", False), (".abc@abc.com", False),
                  ("abc()*@gmail.com", False), ("abc@%*.com", False),
                  ("abc..2002@gmail.com", False), ("abc.@gmail.com", False),
                  ("abc@gmail.com.1a", False)]


@pytest.mark.parametrize("email,expected", list_of_emails)
def test_email(email, expected):
    user_registration = UserRegistration()
    assert user_registration.validate_email(email) == expected
