# Megan Lane

# 4/9/2024

# P4HW2

# Make a pay rate using a while loop for multiple employees

# Set all counters to zero
num_employ = 0
total_hours_pay = 0
total_hours_over_pay = 0
total_gross = 0

# The name is the while variable, otherwise Done will terminate the while loop
employ_name = input("Enter employee's name or 'Done' to terminate: ")
# The loop is based on the variable for employ name not to equal Done
while employ_name != "Done":
    # First counter for number of employees calced
    num_employ += 1
    # Previous code to calc payrate
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

    # Other 3 counters for regular pay, overtime pay, and gross
    total_hours_pay += hours_payed
    total_hours_over_pay += hours_over_payed
    total_gross += total_payed

    # Offers ability to end the loop by entering Done
    employ_name = input("Enter employee's name or 'Done' to terminate: ")
    
# Print results of the counters while using the 'while loop'
print(f"num of employees calculated for {num_employ}")
print(f"Total regular pay is {total_hours_pay}")
print(f"Total overtime pay is {total_hours_over_pay}")
print(f"Total overall pay is {total_gross}")

