import random
import string

def password_gen(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length < 4:
                print("Password length should be at least 4 characters for security.")
            else:
                password = password_gen(length)
                print(f"Generated Password: {password}")
                break
        except ValueError:
            print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
