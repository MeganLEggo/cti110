# I was supposed to put a comment here
# Megan Lane
#3/19/2024
#P3HW1
#Debugging


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules ## now all floats

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: ')) ## fixed the alignment
mod_3 = float(input('Enter grade for Module 3: ')) ## insert close ', fixed var name
mod_4 = float(input('Enter grade for Module 4: ')) ## Fixed text, fixed var name
mod_5 = float(input('Enter grade for Module 5: ')) ## Fixed var name
mod_6 = float(input('Enter grade for Module 6: ')) ## Fixed the ', fixed the allignment, fixed var name 




# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6] ## Fixed var names, included mod_6, and comma




# TO DO: determine lowest, highest , sum and average for grades

low = min(grades) ## Fixed var name grades
high = max(grades) ## Fixed function
summ_of = sum(grades) ## Fixed var name, NEED float
avg = sum(grades) / len(grades) ##insert avg eq

print('-------------Results--------------')
print('Lowest Grade:', low)
print('Highest Grade:', high)
print('Sum of Grades:', summ_of)
print(f'Average: {avg:.2f}')
print('----------------------------------')


# determine letter grade for average

if avg >= 90:
 print('Your grade is: A') ##indent 
elif avg >= 80: ## Fixed to >=, fixed var name
 print('Your grade is: B')
else:
 print('Your grade is: F') # TO DO: finish this





