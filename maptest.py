import turtle
from time import sleep
POSITIONSX = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
POSITIONSY = ['1','2','3','4','5','6','7','8','9','10']

def identificationlettres(i, POSITIONS):

    if i == 9:

        turtle.penup()
        turtle.setpos(-382, 275-((i)*63))
        turtle.write(POSITIONS[i], font=("Arial", 30, "normal"))
    
    else:
        turtle.penup()
        turtle.setpos(-364, 275-((i)*63))
        turtle.write(POSITIONS[i], font=("Arial", 30, "normal"))

def identificationchiffres(i, POSITIONS):

    if i < 10:
        if i == 8:
        
            turtle.penup()
            turtle.setpos(-302+(i*54), 335)
            turtle.write(POSITIONS[i], font=("Arial", 30, "normal"))

        else:

            turtle.penup()
            turtle.setpos(-314+(i*54), 335)
            turtle.write(POSITIONS[i], font=("Arial", 30, "normal"))

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
        turtle.penup()
        turtle.setpos(k, 325)
        turtle.pos()
        while i < 10:

            turtle.setpos(k, 325-(i*70))
            turtle.pos()
            turtle.pendown()
            if j == 0:
                identificationlettres(i, POSITIONSY)
                turtle.setpos(k, 325-(i*70))
                turtle.pendown()
            i += 1
        j += 1

    while l < 11:

        i = 0
        a = 325-(l*63)
        turtle.penup()
        turtle.setpos(-324, a)
        turtle.pos()
        while i < 11:

            turtle.setpos(-324-(i*-54), a)
            turtle.pos()
            turtle.pendown()
            if l == 0:
                identificationchiffres(i, POSITIONSX)
                turtle.setpos(-324-(i*-54), a)
                turtle.pendown()

            i += 1
        l += 1
    turtle.hideturtle()

createmap()