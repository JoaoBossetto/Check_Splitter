print("Welcome to the tip calculator! ")
total_bill = float(input("What was the total bill? "))
tip = float(input("What porcentage tip would you like to give? "))
people_number = float(input("How many people to split the bill? "))

total_to_pay = (total_bill + (total_bill * tip//100))
total_split = (total_to_pay / people_number)
print(f"Each person has to pay ${total_split} ")

