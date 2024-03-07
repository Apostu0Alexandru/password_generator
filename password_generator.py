import random;

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_+"

def generate_password (length=12):
    password = ""
    for _ in range (length):
        password +=random.choice(lowercase_letters+uppercase_letters+digits+symbols)
    return password

def display_password (password):
    print ("Your random generated password is:", password)

password = generate_password()
display_password(password)