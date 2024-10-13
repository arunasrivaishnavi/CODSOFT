import random
import string
def password_generator():
    length = int(input("Enter the password length: "))
    print("Choose a password complexity:")
    print("1. Low (only letters)")
    print("2. Medium (letters and numbers)")
    print("3. High (letters, numbers, and special characters)")
    complexity = int(input("Enter your choice (1/2/3): "))
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid choice. Defaulting to high complexity.")
        characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated Password: {password}")

password_generator()