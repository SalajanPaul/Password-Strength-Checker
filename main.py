import string

def check_password_strength(password):
    strength = 0
    remarks = " "
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == " ":
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = ("That's a very bad password."
                   " Change it as soon as possible.")

    elif strength == 2:
        remarks = ("That's a weak password."
                   " You should change it!")

    elif strength == 3:
        remarks = "That's a good password, but you could improve it!"

    elif strength == 4:
        remarks = "That's a very good password!"

    elif strength == 5:
        remarks = "That's an amazing password!"

    print(f"Your password is {password} and have: ")
    print(f"{lower_count} lowercase letters")
    print(f"{upper_count} uppercase letters")
    print(f"{num_count} digits")
    print(f"{wspace_count} whitespaces")
    print(f"{special_count} special characters")
    print(f"Password score: {strength} from 5")
    print(f"Remarks: {remarks}")


if __name__ == '__main__':
    print('===== Welcome to Password Strength Checker =====')
    user_password = input("Password: ")
    check_password_strength(user_password)