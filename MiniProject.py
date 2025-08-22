def check_password(password):
    if len(password) < 8:
        return "Password must be more than 8 characters."

    has_upper = False
    has_lower = False
    has_special = False
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"   



    # we are verifing the password

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char in special_characters:
            has_special = True

    if not has_upper:
        return "Password must have at least one uppercase letter."
    if not has_lower:
        return "Password must have at least one lowercase letter."
    if not has_special:
        return "Password must have at least one special character."

    return "Password is strong!"


# Taking input from user
user_password = input("Enter your password: ")
result = check_password(user_password)
print(result)