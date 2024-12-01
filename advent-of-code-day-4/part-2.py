import re

inpFile = open("input.txt", "r")

inp = inpFile.read()
linesArr = inp.split("\n")
inpFile.close()

numCards = 0
doLaterLinesArr = []

def doThisLaterThing(m):
    for m in doLaterLinesArr:
        print("card: " + str(m+1))
        doTheThing(m)

def doTheThing(lineI):
    matches = 0
    global numCards
    numCards += 1

    print()
    print("card: " + str(lineI + 1))
    
    line = linesArr[lineI]
    cardArr = re.sub(r"\s+", " ", re.sub(r"Card\s+\d+:\s+", "", line)).split(" | ")
    wNumsArr = cardArr[0].split(" ")
    gNumsArr = cardArr[1].split(" ")
    for wNum in wNumsArr:
        for gNum in gNumsArr:
            if gNum == wNum:
                matches += 1

    if matches > 0:
        for m in range(lineI + 2, lineI + matches + 2):
            doLaterLinesArr.append(m)
            doThisLaterThing(m)

for line in linesArr:
    lineI = linesArr.index(line)
    doTheThing(lineI)

print('\n\n\n')
print(numCards)