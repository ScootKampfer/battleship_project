import random
from time import sleep

POSITIONSX = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
POSITIONSY = ['1','2','3','4','5','6','7','8','9','10']
PositionsOccupeesBateau = []

#partie choisir des bateaux

def taketerritory():

    PositionsOccupeesBateau.append(str().join(positionDebut))
    PositionsOccupeesBateau.append(str().join(positionFin))
    print(PositionsOccupeesBateau)

def poserbateau(boatlength):
    global positionFin
    global positionDebut
    n = 1
    positionFin = []
    positionDebut = [random.choice(POSITIONSX[-1+boatlength:11-boatlength]) ,random.choice(POSITIONSY[-1+boatlength:11-boatlength])]
    PositionsOccupeesBateau.append(str().join(positionDebut))
    orientation = random.randint(1,4)
    match orientation:

        case 1: #Nord
            
            while n < boatlength:
                positionFin = [positionDebut[0], str(POSITIONSY[POSITIONSY.index(positionDebut[1])+n])]
                PositionsOccupeesBateau.append(str().join(positionFin))
                n += 1

        case 2: #Sud
            
            while n < boatlength:
                positionFin = [positionDebut[0], str(POSITIONSY[POSITIONSY.index(positionDebut[1])+n])]
                PositionsOccupeesBateau.append(str().join(positionFin))
                n += 1
        
        case 3: #Est 

            while n < boatlength:
                positionFin = [POSITIONSX[POSITIONSX.index(positionDebut[0]) + n], positionDebut[1]]
                PositionsOccupeesBateau.append(str().join(positionFin))
                n += 1
        
        case 4: #Ouest
                
                while n < boatlength:
                    positionFin = [POSITIONSX[POSITIONSX.index(positionDebut[0]) - n], positionDebut[1]]
                    PositionsOccupeesBateau.append(str().join(positionFin))
                    n += 1

i = 0

while i < 50:
    poserbateau(3)
    print(PositionsOccupeesBateau)
    PositionsOccupeesBateau.clear()
    i += 1

# positionTir = list(input("Ou voulez-vous tirer ex: A1, J9?: ").capitalize())


# if positionTir[0] in POSITIONSX and positionTir[1] in POSITIONSY:

    #sleep(0.00000001)

#else:
    #positionTir = list(input("S'il vous plait, ?: ").capitalize())
    

# Partie "relation" (Juju)

