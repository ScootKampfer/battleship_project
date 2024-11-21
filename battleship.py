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

#Partie Humain (complet)

print("Bienvenue à Battleship! Il est maintenant temps de choisir tes positions de bateau!\n")

def taketerritory(player):

    if player == "Humain":
    
        global i
        PositionsprisesHumain.append(str(positionDebutH))
        PositionsprisesHumain.append(str(positionFinH))
        i += 1
        print(PositionsprisesHumain)
    
    elif player == "AI":

        print("Code to be put here")


def poserbateaujoueur(boatnumber):
    global i 
    i = 0
    PosValid = False
    global positionDebutH
    global positionFinH
    positionDebutH = list(input("Indiquez la position de départ du bateau à deux places comme ceci (A5 ou B6): "))
    positionFinH = None

    while i < boatnumber:

        while PosValid == False:

            positionDebutH = list(input("Indiquez la position de départ du bateau à deux places comme ceci (A5 ou B6): "))
            if positionDebutH[0] in POSITIONSX and positionDebutH[1] in POSITIONSY:
                PosValid = True


        while positionFinH == None:

            orientation = input("\nChoisir l'orientation du bateau (Nord, Sud, Est ou Ouest): ")

            if orientation == "Nord":
                if positionDebutH[1] == '1':

                    print("Try again pls")
                    continue
                else:  
                    positionFinH = [positionDebutH[0], str(POSITIONSY.index(positionDebutH[1]))]
                    taketerritory("Humain")

            elif orientation == "Sud":
                if positionDebutH[1] == '10':

                    print("Try again pls")
                    continue
                else:  
                    positionFinH = [positionDebutH[0], str(POSITIONSY.index(positionDebutH[1])+2)]
                    taketerritory("Humain")

            elif orientation == "Est":
                if positionDebutH[0] == 'J':

                    print("Try again pls")
                    continue
                else:  
                    positionFinH = [POSITIONSX[POSITIONSX.index(positionDebutH[0]) + 1], positionDebutH[1]]
                    taketerritory("Humain")


            elif orientation == "Ouest":
                if positionDebutH[0] == 'A':

                    print("Try again pls")
                    continue
                else:  
                    positionFinH = [POSITIONSX[POSITIONSX.index(positionDebutH[0]) - 1], positionDebutH[1]]
                    taketerritory("Humain")

poserbateaujoueur(2)

# Partie "relation" (Juju)

