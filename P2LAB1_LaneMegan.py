# Megan Lane

# 2/29/2024

# P2LAB1

# Driving Costs

car_mi = float(input("Enter car's mile per gallon: "))
gas_cost = float(input("Enter gas dollars per gallon: "))

travel_cost_20 = float((20/car_mi) * gas_cost)
travel_cost_75 = float((75/car_mi) * gas_cost)
travel_cost_500 = float((500/car_mi) * gas_cost)

print("20 mile travel cost:", end=" ")
print(f'{travel_cost_20:.2f}')   

print("75 mile travel cost:", end=" ")
print(f'{travel_cost_75:.2f}')

print("500 mile travel cost:", end=" ")
print(f'{travel_cost_500:.2f}')
