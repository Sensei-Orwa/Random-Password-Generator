import random
import string

length = int(input("Enter the length of your password: "))



chars = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(length):
    next_character = random.choice(chars)
    password += next_character

print(password)