import random
import string

def create_random_password():
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(random.randint(8, 16)))
    return password

def is_password_acceptable(password, dictionary):
    # Check if the password contains at least one special symbol and is not a word in the dictionary
    if any(char in string.punctuation for char in password) and password not in dictionary:
        return True
    return False

def password_simulator():
    accepted_passwords = []
    dictionary_list = ["password", "123456", "qwerty"]  # Example dictionary list
    iterations = 0

    while iterations < 40:
        random_password = create_random_password()
        if is_password_acceptable(random_password, dictionary_list):
            accepted_passwords.append(random_password)
            print(f"Accepted: {random_password}")
        else:
            print("Unaccepted password, deleted.")
        iterations += 1

    # Archive accepted passwords
    with open('accepted_passwords.txt', 'w') as file:
        for password in accepted_passwords:
            file.write(f"{password}\n")

    print(f"Simulation completed. {len(accepted_passwords)} passwords accepted and archived.")

password_simulator()
