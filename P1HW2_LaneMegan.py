# Megan Lane
# 2/15/2024
# P1HW2
# Make a budget and calculate costs

Budget  = float(input("Enter your budget amount:\n"))
Dest    = input("Enter travel destination:\n")
Gas     = float(input("Enter the estimated amount you will spend on gas:\n"))
Accom   = float(input("Enter the estimated amount you will spend on accomodation:\n"))
Food    = float(input("Enter the estimated amount you will spend on food:\n"))
Total_spend = Gas + Accom + Food
Leftover = Budget - Total_spend
print("-----------Travel Expenses-----------\n")
print("Location:", Dest)
print("Initial Budget:", Budget)
print("\nFuel:", Gas)
print("Accomodation:", Accom)
print("Food:", Food)
print("\nTotal Cost:", Total_spend)
print("\nRemaining Balance:", Leftover, "\n")

