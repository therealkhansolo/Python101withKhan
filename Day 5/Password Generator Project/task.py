import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# letters_chosen = random.sample(letters, k = nr_letters)
# symbols_chosen = random.sample(symbols, k = nr_symbols)
# numbers_chosen = random.sample(numbers, k = nr_numbers)
#
# new_password = letters_chosen + symbols_chosen + numbers_chosen
#
# print(f"{new_password}")
# random.shuffle(new_password)
# print(f"{new_password}")
# print(f"Your new password is: {str(random.sample(new_password, k = (nr_numbers + nr_symbols + nr_letters)))}")

#SOLUTION: EASY VERSION

# password = ""
#
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
#
# for sym in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#
# for num in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
#
# print(password)

#SOLUTION: HARD VERSION
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for sym in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for num in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is : {password}")