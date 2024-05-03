#Megan Lane

#3/31/2024

#P4LAB1-A

# Turtle!



import turtle
wn = turtle.Screen()
Mac = turtle.Turtle()
Mac.shape("turtle")

for i in [0,1,2,3]:
    Mac.forward(50)
    Mac.left(90)

Mac.forward(20)

for am in [0,1,2,3]:
    Mac.right(120)
    Mac.forward(50)


wn.mainloop()
