import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the ultimate Password Generator")
password_result = []


letter_input = int(input("How many letters would you like in your password?"))
for letter in range(0, letter_input):
    password_result.append(random.choice(letters))


symbol_input = int(input("How many symbols would you like in your password?"))
for symbol in range(0, symbol_input):
    password_result.append(random.choice(symbols))


number_input = int(input("How many numbers would you like in your password?"))
for number in range(0, number_input):
    password_result.append(random.choice(numbers))

random.shuffle(password_result)



print(f"Here is your password: {''.join(password_result)}")