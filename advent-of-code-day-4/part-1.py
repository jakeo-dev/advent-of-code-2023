import re

inpFile = open("input.txt", "r")

inp = inpFile.read()
linesArr = inp.split("\n")
inpFile.close()

totalPoints = 0

for line in linesArr:
    cardArr = re.sub(r"\s+", " ", re.sub(r"Card\s+\d+:\s+", "", line)).split(" | ")
    wNumsArr = cardArr[0].split(" ")
    gNumsArr = cardArr[1].split(" ")
    points = 0
    for wNum in wNumsArr:
        for gNum in gNumsArr:
            if gNum == wNum:
                if points == 0:
                    points += 1
                else:
                    points *= 2

    totalPoints += points

print(totalPoints)