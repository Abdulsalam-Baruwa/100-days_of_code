print("Welcome to the tip calculator.")

bill = input("What was the total bill?\n$")
bill_as_a_float = float(bill)

tip = int(input("What percentage tip would you like to give? e.g. 10, 12 or 15?\n"))

tip_percentage = (tip/100) * bill_as_a_float
total_bill = bill_as_a_float + tip_percentage

people = int(input("How many people to split the bill? \n"))
split = "{:.2f}".format(total_bill/people)

print(f"The total bill plus tip is ${total_bill}\nEach person should pay: ${split}")