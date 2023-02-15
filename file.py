import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

#           По умолчанию пароль генерируется с числами, символами
#           Если (<любое число>, False, False) - пароль будет только с буквами


    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

#           Добавятся числа и символы, если они нужны по условию


    pwd = ''
    meets_criteria = False
    has_number = False
    has_special = False

    
    

    print(letters, digits, special)



generate_password(10)