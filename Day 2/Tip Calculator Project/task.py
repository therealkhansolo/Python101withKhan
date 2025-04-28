print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? R"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_total = ((tip/100) * bill)
bill_total = (bill + tip_total)
bill_per_person = bill_total / people
print(f"Each person should pay: R{round(bill_per_person, 2)}")