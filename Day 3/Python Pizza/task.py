print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# Set the base price for the pizza
if size == 'S':
    pizza_price = 15
elif size == 'M':
    pizza_price = 20
elif size == 'L':
    pizza_price = 25
else:
    print("Invalid pizza size.")
    pizza_price = 0

# Add pepperoni cost based on pizza size
if pepperoni == 'Y':
    if size == 'S':
        pizza_price += 2
    else:
        pizza_price += 3

# Add extra cheese cost
if extra_cheese == 'Y':
    pizza_price += 1

# Print the final bill
print(f"Your final bill is: ${pizza_price}.")


