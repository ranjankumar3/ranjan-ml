import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length for the password: "))
        if length <= 0:
            print("Please enter a positive integer for the password length.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
