import random
import turtle
from termcolor import colored

POSITIONSX = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
POSITIONSY = ['1','2','3','4','5','6','7','8','9','10']
PositionsOccupeesBateau = []
PositionsEssayees = []
Porte_Avion = []
Croiseur = []
Contre_Torpilleur = []
Sous_Marin = []
Torpilleur = []
e = 0

screen = turtle.Screen()
screen.tracer(0,0)

def identification(i, POSITIONS, type_de_lettres):
    
    turtle.penup()

    if type_de_lettres == "Lettres":
        if i == 9:
            turtle.setpos(-382, 275-((i)*63))
        
        else:
            turtle.setpos(-364, 275-((i)*63))
    
    if type_de_lettres == "Chiffres":
        if i < 10:
            if i == 8:
                turtle.setpos(-302+(i*54), 335)
            else:
                turtle.setpos(-314+(i*54), 335)

    if i != 10:
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
                identification(i, POSITIONSY, "Lettres")
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
                identification(i, POSITIONSX, "Chiffres")
                turtle.setpos(-324-(i*-54), a)
                turtle.pendown()

            i += 1
        l += 1
        
    turtle.hideturtle()
    screen.update()

def mark(positionasked, status):

    listposition = list(positionasked)
    if len(listposition) == 3:
        listposition[1] = listposition[1]+listposition[2]
        listposition = listposition[0:2]
    x = -314 + (POSITIONSX.index(listposition[0])*54)
    y = 275 - (POSITIONSY.index(listposition[1])*63)
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pos()
    turtle.pendown()
    if status == "Touché":
        turtle.color("red")
        turtle.write("X", font=("Arial", 20, "normal"))
    elif status == "Manqué!":
        turtle.color("black")
        turtle.write("M", font=("Arial", 20, "normal"))

def checkterritory():

    global TerritoryVerified

    for i in PositionsPotentiels:
        if i in PositionsOccupeesBateau:
            break
        PositionsOccupeesBateau.append(str(i))
    TerritoryVerified = True

def poserbateau(boatlength):

    global positionsBateauChoisi
    global TerritoryVerified
    global PositionsPotentiels
    TerritoryVerified = False
    n = 1
    positionFin = []
    PositionsPotentiels = []
    positionsBateauChoisi = []

    while TerritoryVerified == False:

        positionDebut = [random.choice(POSITIONSX[-1+boatlength:11-boatlength]) ,random.choice(POSITIONSY[-1+boatlength:11-boatlength])]
        positionsBateauChoisi.append(str().join(positionDebut))
        PositionsPotentiels.append(str().join(positionDebut))
        orientation = random.randint(1,4)
        while n < boatlength:

            match orientation:

                case 1: #Nord
                    positionFin = [positionDebut[0], str(POSITIONSY[POSITIONSY.index(positionDebut[1])+n])]

                case 2: #Sud
                    positionFin = [positionDebut[0], str(POSITIONSY[POSITIONSY.index(positionDebut[1])-n])]
                
                case 3: #Est 
                    positionFin = [POSITIONSX[POSITIONSX.index(positionDebut[0]) + n], positionDebut[1]]
                
                case 4: #Ouest
                    positionFin = [POSITIONSX[POSITIONSX.index(positionDebut[0]) - n], positionDebut[1]]
  
            PositionsPotentiels.append(str().join(positionFin))
            positionsBateauChoisi.append(str().join(positionFin))
            n += 1

        checkterritory() 

def checkvalidcoordinate():

    global positionTir
    AttackVerified = False

    while AttackVerified == False:
        positionTir = list(input("Ou voulez-vous tirer? S'il vous plait entrez les coordonnées comme ça: A1, J9: ").capitalize())
        
        if len(positionTir) < 2:
            continue

        if len(positionTir) > 2:
            positionTir[1] = positionTir[1]+positionTir[2]
            positionTir = positionTir [0:2]

        if positionTir[0] in POSITIONSX and positionTir[1] in POSITIONSY:
            positionTir = str().join(positionTir)
            AttackVerified = True

        if positionTir in PositionsEssayees:
            AttackVerified = False
            continue

def checkifcoule(boatlist):

    if positionTir in boatlist:
        boatlist.remove(positionTir)
        if len(boatlist) == 0:
           print(colored("Coulé!","green")) 

def checkiftouched():

    PositionsEssayees.append(positionTir)

    if positionTir in PositionsOccupeesBateau:
        PositionsOccupeesBateau.remove(positionTir)
        mark(positionTir, "Touché")
        print(colored("Touché","red"))
        checkifcoule(Porte_Avion)
        checkifcoule(Croiseur)  
        checkifcoule(Contre_Torpilleur) 
        checkifcoule(Sous_Marin)
        checkifcoule(Torpilleur)

    else:
        mark(positionTir, "Manqué!")
        print(colored("Manqué!","blue"))
    
createmap()

while len(PositionsOccupeesBateau) != 17:

    PositionsOccupeesBateau.clear()
    poserbateau(5)
    Porte_Avion = positionsBateauChoisi
    poserbateau(4)
    Croiseur = positionsBateauChoisi
    poserbateau(3)
    Contre_Torpilleur = positionsBateauChoisi
    poserbateau(3)
    Sous_Marin = positionsBateauChoisi
    poserbateau(2)
    Torpilleur = positionsBateauChoisi

while True:

    checkvalidcoordinate()
    checkiftouched()
    e += 1

    if len(PositionsOccupeesBateau) == 0:
        print(f"Bravo, tu as gagné avec {e} essais!")
        exit()