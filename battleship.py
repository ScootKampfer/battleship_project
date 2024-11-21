import random

positionsX = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
positionsY = ['1','2','3','4','5','6','7','8','9','10']
longeurB = 2

#partie ordi among us 

positionsBateauIA_1_1 = [random.choice(positionsX[-1+longeurB:10-longeurB]) ,random.choice(positionsY[-1+longeurB:10-longeurB])]
# positionsBateauIA_1_2 = [positionsX[positionsBateauIA_1_1.index(0)] + random.choice(-1,1)], positionsY[positionsBateauIA_1_1.index(1)] +random.choice(-1,1)]

print(positionsBateauIA_1_1)
#print(positionsBateauIA_1_2)

#partie humain

print("Bienvenue à Battleship! Il est maintenant temps de choisir tes positions de bateau!\n")
positionDebut1H = list(input("Indiquez la position de départ du bateau à deux places comme ceci (A5 ou B6): "))
positionFin1H = None


while positionFin1H == None:

    orientation = input("\nChoisir l'orientation du bateau (Nord, Sud, Est ou Ouest): ")

    if orientation == "Nord":
        if positionDebut1H[1] == '1':

            print("Try again pls")
            continue
        else:  
            positionFin1H = [positionDebut1H[0], positionsY[positionDebut1H.index(positionDebut1H[1])-1]]
            print(positionFin1H)

    if orientation == "Sud":
        if positionDebut1H[1] == '10':

            print("Try again pls")
            continue
        else:  
            positionFin1H = [positionDebut1H[0], positionDebut1H.index()+1]
            print(positionFin1H)

    if orientation == "Est":
        if positionDebut1H[0] == 'J':

            print("Try again pls")
            continue
        else:  
            positionFin1H = [positionDebut1H[0], positionFin1H[positionDebut1H.index()-1]]
            print(positionFin1H)

    if orientation == "Ouest":
        if positionDebut1H[0] == '1':

            print("Try again pls")
            continue
        else:  
            positionFin1H = [positionDebut1H[0], positionFin1H[positionDebut1H.index()-1]]
            print(positionFin1H)


# Partie "relation" (Juju)

