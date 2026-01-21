import random
import string

# Asking user for password length
length = int(input("Enter the length of the password: "))

# Defining characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Password genrating
password = ""
for i in range(length):
    password += random.choice(characters)

# display password
print("Generated Password:", password)
