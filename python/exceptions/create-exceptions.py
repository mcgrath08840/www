class MissingLabelError(KeyError):
    pass

class PageNotFoundError(LookupError):
    pass

class IncorrectPasswordError(ValueError):
    pass

class IncorrectUsernameError(ValueError):
    pass

class APIThrottleLimitError(RuntimeError):
    pass


# Program... user enters wrong username
def login():
    # This raises the specific error that will be called below when run.
    raise IncorrectPasswordError

try:
    login()
except IncorrectUsernameError:
    print("Your username was incorrect.  Have you forgotten it?")
# This exception below runs because specifically raised above.
except IncorrectPasswordError:
    print("Your password was wrong.  Have you forgotten it?")