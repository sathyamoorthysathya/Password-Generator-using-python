import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!?@#$%^&"

combination = lower_case + upper_case + number + symbols
length_of_password = 8
password = "".join(random.sample(combination, length_of_password))
print("The Generated Password is:", password)