passw = input("Enter your password: ")

def check_password_strength(password):
    error = []

    if len(password) < 8:
        error.append("at least 8 characters")
    if not any(i.isdigit() for i in password):
        error.append("at least one digit")
    if not any(i.islower() for i in password):
        error.append("at least one lowercase letter")
    if not any(i.isupper() for i in password):
        error.append("at least one uppercase letter")
    if not any(i in '!@#%^&(*)' for i in password):
        error.append("at least one special character ")

    if error:
        return f"Weak password. It should contain: {', '.join(error)}."
    else:
        return "Strong password."

print(check_password_strength(passw))
