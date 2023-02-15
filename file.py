import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    print(letters, digits, special)

#           По умолчанию пароль генерируется с числами, символами
#           Если (<любое число>, False, False) - пароль будет только с буквами


generate_password(10, False, False)