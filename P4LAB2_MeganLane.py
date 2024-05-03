# Megan Lane

# 4/9/2024

# PW4LAB2

# An incremental loop

# The input numbers from the user
var = int(input())
var2 = int(input())

# Try the for loop
if var < var2:
    for var in range(var, var2, 5):
        print(var, end=" ")
    print(var2)
elif var > var2:
    print("Second integer can't be less than the first.")
else:
    print(var)
