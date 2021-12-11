class UserRegistrationException(Exception):
    """Raised when the input value is none and empty"""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
