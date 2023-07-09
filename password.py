"""
The verification conditions are:

- the length should be bigger than 6;
- should contain at least one digit, but it cannot consist of just digits;
- having numbers or containing just numbers does not apply to the password longer than 9;
- a string should not contain the word "password" in any case.
"""
import random
import string

def is_acceptable_password(password: str) -> bool:
    cond1 = len(password) > 6
    cond2 = any(map(str.isdigit, password))
    cond3 = any(map(str.isalpha, password))
    if len(password) > 9:
        cond2 = cond3 = True
    cond5 = "password" not in password.lower()
    return all([cond1, cond2, cond3, cond5])

def generate_password():
    while True:
        length = random.randint(7,15)   # Random password length between 7 and 15 characters
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        
        if is_acceptable_password(password):
            return password

print(generate_password())




