import random

POSITIONSX = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
POSITIONSY = ['1','2','3','4','5','6','7','8','9','10']
PositionsOccupeesBateau = []

def checkterritory():

    global TerritoryVerified

    for i in PositionsPotentiels:
        if i in PositionsOccupeesBateau:
            break
        PositionsOccupeesBateau.append(str(i))
    TerritoryVerified = True


def poserbateau(boatlength):

    global TerritoryVerified
    global PositionsPotentiels
    TerritoryVerified = False
    n = 1
    positionFin = []
    PositionsPotentiels = []
    positionDebut = [random.choice(POSITIONSX[-1+boatlength:11-boatlength]) ,random.choice(POSITIONSY[-1+boatlength:11-boatlength])]
    PositionsPotentiels.append(str().join(positionDebut))
    orientation = random.randint(1,4)
    while TerritoryVerified == False:

        while n < boatlength:

            match orientation:

                case 1: #Nord
                    positionFin = [positionDebut[0], str(POSITIONSY[POSITIONSY.index(positionDebut[1])+n])]

                case 2: #Sud
                    positionFin = [positionDebut[0], str(POSITIONSY[POSITIONSY.index(positionDebut[1])+n])]
                
                case 3: #Est 
                    positionFin = [POSITIONSX[POSITIONSX.index(positionDebut[0]) + n], positionDebut[1]]
                
                case 4: #Ouest
                    positionFin = [POSITIONSX[POSITIONSX.index(positionDebut[0]) - n], positionDebut[1]]
  
            PositionsPotentiels.append(str().join(positionFin))
            n += 1

        checkterritory()

while len(PositionsOccupeesBateau) != 17:
    PositionsOccupeesBateau.clear()
    poserbateau(5)
    poserbateau(4)
    poserbateau(3)
    poserbateau(3)
    poserbateau(2)

# positionTir = list(input("Ou voulez-vous tirer ex: A1, J9?: ").capitalize())


# if positionTir[0] in POSITIONSX and positionTir[1] in POSITIONSY:

    #sleep(0.00000001)

#else:
    #positionTir = list(input("S'il vous plait, ?: ").capitalize())
    

# Partie "relation" (Juju)

