import random
import string

def generate_password():
    try:
        length = int(input("Enter desired password length (minimum 10): "))

        if length < 10:
            print("Password length must be at least 10 characters.")
            return

        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special_chars = string.punctuation

        all_chars = lowercase + uppercase + digits + special_chars

        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(special_chars)
        ]

        remaining_length = length - 4
        password += random.choices(all_chars, k=remaining_length)

        random.shuffle(password)

        final_password = "".join(password)

        print("\nGenerated Strong Password:")
        print(final_password)

    except ValueError:
        print("Invalid input! Please enter a valid number.")

generate_password()
    