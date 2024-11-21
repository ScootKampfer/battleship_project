import random

POSITIONSX = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
POSITIONSY = ['1','2','3','4','5','6','7','8','9','10']
PositionsprisesIA = []
PositionsprisesHumain = []
longeurB = 2

#partie ordi among us 

positionsBateauIA_1_1 = [random.choice(POSITIONSX[-1+longeurB:10-longeurB]) ,random.choice(POSITIONSY[-1+longeurB:10-longeurB])]
# positionsBateauIA_1_2 = [positionsX[positionsBateauIA_1_1.index(0)] + random.choice(-1,1)], positionsY[positionsBateauIA_1_1.index(1)] +random.choice(-1,1)]

print(positionsBateauIA_1_1)
#print(positionsBateauIA_1_2)

#partie humain

print("Bienvenue à Battleship! Il est maintenant temps de choisir tes positions de bateau!\n")

def taketerritory():

    global i
    PositionsprisesHumain.append(str(positionDebut1H))
    PositionsprisesHumain.append(str(positionFin1H))
    i += 1
    print(PositionsprisesHumain)

def poserbateaujoueur(boatnumber):
    global i 
    i = 0

    while i < boatnumber:

        global positionDebut1H
        global positionFin1H
        positionDebut1H = list(input("Indiquez la position de départ du bateau à deux places comme ceci (A5 ou B6): "))
        positionFin1H = None


        while positionFin1H == None:

            orientation = input("\nChoisir l'orientation du bateau (Nord, Sud, Est ou Ouest): ")

            if orientation == "Nord":
                if positionDebut1H[1] == '1':

                    print("Try again pls")
                    continue
                else:  
                    positionFin1H = [positionDebut1H[0], str(POSITIONSY.index(positionDebut1H[1]))]
                    taketerritory()

            elif orientation == "Sud":
                if positionDebut1H[1] == '10':

                    print("Try again pls")
                    continue
                else:  
                    positionFin1H = [positionDebut1H[0], str(POSITIONSY.index(positionDebut1H[1])+2)]
                    taketerritory()

            elif orientation == "Est":
                if positionDebut1H[0] == 'J':

                    print("Try again pls")
                    continue
                else:  
                    positionFin1H = [POSITIONSX[POSITIONSX.index(positionDebut1H[0]) + 1], positionDebut1H[1]]
                    taketerritory()


            elif orientation == "Ouest":
                if positionDebut1H[0] == 'A':

                    print("Try again pls")
                    continue
                else:  
                    positionFin1H = [POSITIONSX[POSITIONSX.index(positionDebut1H[0]) - 1], positionDebut1H[1]]
                    taketerritory()

poserbateaujoueur(2)

# Partie "relation" (Juju)

