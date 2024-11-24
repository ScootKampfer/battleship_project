POSITIONSX = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
POSITIONSY = ['1','2','3','4','5','6','7','8','9','10']
coordinates = []
huh = 0
huhwhy = 0

for i in POSITIONSX:

    huhwhy = 0

    for i in POSITIONSY:

        coordinates.append(f"{POSITIONSX[huh]}{POSITIONSY[huhwhy]}")
        huhwhy += 1
    huh += 1

print(str(" = ").join(coordinates) + " = 0")