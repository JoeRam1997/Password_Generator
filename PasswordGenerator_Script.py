# Import the necessary modules
import random
import string

# Welcome Statement
print("Hola, Welcome to your Password Generator!")

# Input the length of the password
length = int(input('\nEnter the length needed for the password please:'))

# Define password requirements
upper = string.ascii_uppercase
lower = string.ascii_lowercase
num = string.digits
symbols = string.punctuation

# Combine the requirements to form the password
all = upper + lower + num + symbols

# Randomizing each character
temp = random.sample(all, length)

# Create the password
password = "".join(temp)

# Display the generated password
print(password)














