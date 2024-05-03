# Megan Lane

# 3/19/2024

# P3HW2

# Make a pay rate

employ_name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
employ_pay = float(input("Enter the employee's pay rate: "))
overtime_pay = float(input("Enter the pay rate for overtime: "))
hours_over = hours - 40

if hours >= 40:
    hours_payed = 40 * employ_pay
    hours_over_payed = hours_over * overtime_pay 
else:
    hours_payed = hours * employ_pay
    hours_over_payed = 0

total_payed = hours_payed + hours_over_payed


print('--------------------------------------------')
print('Employee Name:', employ_name)
print('Hours Worked |     ', end=" ")
print('| Pay Rate |     ', end=" ")
print('| OverTime |     '    , end=" ")
print('| OverTime Pay |     ', end=" ")
print('| RegHour Pay |     ', end=" ")
print('| Gross Pay |     ')
print('--------------------------------------------------------------------------------------------------------------------------------')
print(f'{hours:<22.2f}{employ_pay:<18.2f}{hours_over:<19.2f}{hours_over_payed:<21.2f}{hours_payed:<21.2f}{total_payed:<20.2f}')
