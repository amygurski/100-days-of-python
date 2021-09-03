# Calculates how much each person should pay including tip

print("Welcome to the split-the-bill calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 15, 20, or 25? ")) / 100
people = int(input("How many people to split the bill? "))

total_tip = bill * tip
total_bill = bill + total_tip
bill_per_person = total_bill / people

print(f"Each person should pay: ${round(bill_per_person, 2)}")
