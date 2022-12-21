print("Welcome to the tip calculator.")
total_bill = input("How much was the bill? $")
percentage = input("How much of a percentage of a tip would you like to give? 10, 12, or 15? ")
tip_percentage = 1 + (float(percentage) / 100)
num_people = input("How many people will we be splitting the bill by?")
result = (int(total_bill) / int(num_people)) * tip_percentage
print(round(result, 4))