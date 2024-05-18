print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
people = int(input("How many people will split the bill? "))
tip = int(input("How much would you like to tip? '10%' '12%' '15%': "))
tip_percent = tip/100
total_tip = bill * tip_percent
total_bil = bill + total_tip
bill_per_person = total_bil/people

print("{:.2f}".format(bill_per_person))
