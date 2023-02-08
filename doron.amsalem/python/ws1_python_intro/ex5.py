import re


def password_check(password):
    """gets password and return if is correct"""
    return len(password) > 7 and \
           (any(map(str.isdigit, password))) and \
           bool(re.match(r'\w*[A-Z]\w*', password)) and \
           bool(re.match(r'\w*[a-z]\w*', password)) and \
           '@' in password or '#' in password or '%' in password or '&' in password


check = input("insert password: ")
if password_check(check):
    print("password match the pattern")
else:
    print("change password")
