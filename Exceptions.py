class ATMException(Exception):
    def __init__(self, message):
        self.message = message

class AccountNotFound(ATMException):
    pass

class InsufficientBalance(ATMException):
    pass

class InvalidPin(ATMException):
    pass



