# Megan Lane

# 4/9/2024

# P4HW1

# a score calc in a loop

# grade = "none"
var = 1
ask_grade = []
#The var that impacts the loop
total_score = int(input("How many scores will you Enter? Othewise enter '0' to terminate: "))
# how to initiate the loop with a while loop
for i in range(total_score):
# how to produce number of inputs based on total_score number
# take the total_score value, and produce that many inputs
# have a variable that uniquely identifies each input and numbers each of the inputs based on the total_score input
    grade_input = float(input(f"Grade #{var}:"))
    if grade_input > 0:
        ask_grade.append(grade_input)
        var += 1
    elif grade_input < 0:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        grade_input = input(f"Grade #{var} again: ")
        ask_grade.append(grade_input)
        var += 1
    else:
        ask_grade.append(grade_input)
        var += 1
print(ask_grade)
low_score = min(ask_grade)
ask_grade.remove(low_score)
avg_score = sum(ask_grade) / len(ask_grade)

if avg_score <= 90:
    grade = "A"
elif avg_score <= 80:
    grade = "B"
elif avg_score <= 70:
    grade = "C"
elif avg_score <= 60:
    grade = "D"
else:
    grade = "Failure"
    
                        
print('----------------------RESULTS------------------------')
print(f"Lowest Score: {low_score}")
print(f'Modified List without Lowest Score: {ask_grade}')
print(f'Scores Average: {avg_score}')
print(f'Grade: {grade}')
print('-----------------------------------------------------')

                        
    
              
            
