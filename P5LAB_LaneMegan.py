#Megan Lane
# 4/11/2024
# P5LAB
# User-defined function


# Function to determine change returned to customer
def dispurse_change(change):

#Calculate the amount of each coin needed
#integer division - //

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles *5)

    num_pennies = change // 1

    # Displayed coins owed
    if num_dollars > 0:
        print(num_dollars,  end=" ")
        if num_dollars == 1:
            print("Dollar")
        else:
            print("Dollars")
            
    if num_quarters > 0:
        print(num_quarters,  end=" ")
        if num_quarters == 1:
            print("Quarter")
        else:
            print("Quarters")

    if num_dimes > 0:
        print(num_dimes,  end=" ")
        if num_dimes == 1:
            print("Dime")
        else:
            print("Dimes")

    if num_nickles > 0:
        print(num_nickles,  end=" ")
        if num_nickles == 1:
            print("Nickle")
        else:
            print("Nickles")

    if num_pennies > 0:
        print(num_pennies,  end=" ")
        if num_pennies == 1:
            print("Penny")
        else:
            print("Pennies")

# TEST
# Call the Function!
# dispurse_change(1248)

def show_avail_items(dictionary):
    print(f'{"Grocergy Item":<30}{"Price"}')
    print('----------------------------------------------')
    for key, value in dictionary.items():
        print(f'{key:<30}${value:.2f}')
    print('----------------------------------------------')

#MAKE THE WHILE LOOP
def add_items(dictionary):
    cart = []
    choice = input("Enter an item to add to the cart or type 'end' to terminate: ")
    while choice != 'end':
        #If choice is a dictonary key
        if choice in dictionary.keys():
            cart.append(choice)
        else:
            print(f"{choice} is not in stock")
        choice = input("Enter an item to add to the cart or type 'end' to terminate: ")
    #RETURN THE CART
    return cart

def calc_totals(cart, dictionary):
    print("-----------------------------------------------")
    print("Grocery Receipt")
    print("-----------------------------------------------")
    print()
    Subtotal = 0
    for item in cart:
        print(f'{item:<30} ${dictionary[item]:.2f}')
        Subtotal += dictionary[item]
    tax = Subtotal * 0.07
    final_total = tax + Subtotal
    print()
    print(f'{"SUBTOTAL:":<20}{Subtotal:.2f}')
    print(f'{"TAX:":<20}{tax:.2f}')
    print()
    print(f'{" ":<5}{"TOTAL:":<15}{final_total:.2f}')
      
    return Subtotal, tax, final_total
        
#MAIN FUNCTION
def main():
    The_Dictionary = { "apples":3.69, 
                       "berries":4.00, 
                       "chocolate":2.89,  
                       "turkey":6.99, 
                       "cheese":4.00, 
                       "pepsi":7.89, 
                       "eggs":3.50, 
                       "bread":3.00}

    show_avail_items(The_Dictionary)

    #Allow the user to add item to the cart
    cart = add_items(The_Dictionary)
    #print(cart)
    #Show items in cart
    #print("Items in your cart")
    #for item in cart:
     #   print(item)

    Subtotal, tax, final_total = calc_totals(cart, The_Dictionary)

    print()
    inserting = float(input("How much money will you put in the self-checkout? "))
    change_owed = inserting - final_total
    print(f"\nChange will be: ${change_owed:.2f}\n")
    change_owed = change_owed * 100
    dispurse_change(change_owed)
    
#Call the MAIN FUNCTION
main()

