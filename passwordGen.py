import random
import string

length = int(input("Hur långt ska lösenordet vara:"))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print(password)
