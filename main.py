class TooShortError(Exception):
    pass

class TooLongError(Exception):
    pass

class InvalidCharacterError(Exception):
    pass

def validate_string(s):
    if len(s) < 5:
        raise TooShortError("String is too short")
    elif len(s) > 10:
        raise TooLongError("String is too long")
    elif not s.isalpha():
        raise InvalidCharacterError("String contains non-alphabetic characters")

try:
    validate_string("abc")
except TooShortError as e:
    print(e)
except TooLongError as e:
    print(e)
except InvalidCharacterError as e:
    print(e)

try:
    validate_string("abcdefghijklmnopqrstuvwxyz")
except TooShortError as e:
    print(e)
except TooLongError as e:
    print(e)
except InvalidCharacterError as e:
    print(e)

try:
    validate_string("ab123")
except TooShortError as e:
    print(e)
except TooLongError as e:
    print(e)
except InvalidCharacterError as e:
    print(e)







