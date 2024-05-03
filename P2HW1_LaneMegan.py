#Megan

#3/1/2024

#P2HW2

#Modifying P1HW2 and adding floats and dollar signs

print("This program calcuates and displays travel expenses")

Budget = float(input("Enter Budget: "))

Dest = input("Enter your travel destination: ")

Gas = float(input("How much do you think you will spend on gas? "))

Accom = float(input("Approximately how much will you need for accomodation/hotel? "))

Food = float(input("Last, how much do you need for food? "))


Total_spend = Gas + Accom + Food
Leftover = Budget - Total_spend

print("\n-----------Travel Expenses-----------")
print("Location:", Dest)
print("Initial Budget:", f'${Budget:.2f}')
print("Fuel:", f'${Gas:.2f}')
print("Accomodation:", f'${Accom:.2f}')
print("Food:", f'${Food:.2f}')
print("-------------------------------------")

print("\nTotal Cost:", f'${Total_spend:.2f}')

print("\nRemaining Balance:", f'${Leftover:.2f}')

