print("Welcome to the calculator!")
bill = float(input("What was total bill? $"))
tip = int(input("How much tip would you like to give? 10 , 12 , or 15?\n"))
people = int(input("How many people to split the bill?\n"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill_ = bill + total_tip_amount
bill_per_person = total_bill_ / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
