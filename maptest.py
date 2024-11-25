import turtle
from time import sleep
POSITIONSX = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
POSITIONSY = ['1','2','3','4','5','6','7','8','9','10']

def identificationlettres(i, POSITIONSX):


    turtle.penup()
    turtle.setpos(-364, 275-((i)*63))
    turtle.write(POSITIONSX[i], font=("Arial", 30, "normal"))

def createmap():
    j = 0
    l = 0
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-324, 325)
    turtle.pos()

    while j < 11:
        i = 0
        k = -324 + (j*54)
        print(f"For the {j+1} time, here is the value of x: {k}")
        turtle.penup()
        turtle.setpos(k, 325)
        turtle.pos()
        while i < 10:

            turtle.setpos(k, 325-(i*70))
            turtle.pos()
            turtle.pendown()
            if j == 0:
                identificationlettres(i, POSITIONSX)
                turtle.setpos(k, 325-(i*70))
                turtle.pendown()
            i += 1
        j += 1

    while l < 11:

        i = 0
        a = 325-(l*63)
        print(f"For the {l+1} time, here is the value of y: {a}")
        turtle.penup()
        turtle.setpos(-324, a)
        turtle.pos()
        while i < 11:

            turtle.setpos(-324-(i*-54), a)
            turtle.pos()
            turtle.pendown()
            i += 1
        l += 1

createmap()

sleep(3)