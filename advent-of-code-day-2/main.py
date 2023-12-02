import re

inpFile = open("input.txt", "r")

inp = inpFile.read()
gamesArr = inp.split("\n")
inpFile.close()

possibleRed = 12
possibleGreen = 13
possibleBlue = 14

gameNum = 1
sum1 = 0
sum2 = 0

for i in gamesArr:
    thing = i[i.index(":") + 2:]
    thing = thing.split(";")
    possible = True
    allGamesArr = []
    for game in thing: 
        gamesArr = game.split(", ")
        for color in gamesArr:
            if "blue" in color:
                num = int(re.sub(r"(blue)|\s", "", color))
                if num > possibleBlue:
                    possible = False
            elif "green" in color:
                num = int(re.sub(r"(green)|\s", "", color))
                if num > possibleGreen:
                    possible = False
            elif "red" in color:
                num = int(re.sub(r"(red)|\s", "", color))
                if num > possibleRed:
                    possible = False
        allGamesArr = allGamesArr + gamesArr

    blues = []
    greens = []
    reds = []
    for idk in allGamesArr:
        if "blue" in idk:
            blues.append(int(re.sub(r"(blue)|\s", "", idk)))
        elif "green" in idk:
            greens.append(int(re.sub(r"(green)|\s", "", idk)))
        elif "red" in idk:
            reds.append(int(re.sub(r"(red)|\s", "", idk)))
    blues.sort()
    greens.sort()
    reds.sort()
    highestBlue = blues[-1]
    highestGreen = greens[-1]
    highestRed = reds[-1]

    if possible == True:
        sum1 += gameNum

    sum2 += highestBlue * highestGreen * highestRed

    gameNum += 1

print("\nPART 1 SUM: " + str(sum1))
print("PART 2 SUM: " + str(sum2))