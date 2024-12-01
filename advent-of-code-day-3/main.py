import re

inpFile = open("input.txt", "r")
inp = inpFile.read()
inpFile.close()

inpArr = inp.split("\n")
ezInp = re.sub("\n", "", inp)
sum = 0

for line in inpArr:
    numArr = re.findall(r"\d+", line)
    for num in numArr:
        partQuestion = False

        beforeAndAfter = line.split(num)
        pnLineIMin = len(beforeAndAfter[0]) - 1
        pnLineIMax = pnLineIMin + len(str(num)) + 2
        if len(beforeAndAfter) < 2 and re.search(r"^\d", beforeAndAfter[0]):
            pnLineIMin = 0
            numI = re.search(re.escape(num) + r"([^0-9])", line).start()
        if len(beforeAndAfter) < 2 and re.search(r"\d$", beforeAndAfter[0]):
            pnLineIMax = len(line) - 1
            numI = re.search(r"([^0-9])" + re.escape(num), line).start() + 1
        if len(beforeAndAfter[0]) > 0 and len(beforeAndAfter[1]) > 0:
            numI = re.search(r"([^0-9])" + re.escape(num) + r"([^0-9])", line).start() + 1
            
        if len(beforeAndAfter[1]) > 0 and not re.search(r"\.|\d", line[numI + len(str(num))]):
            partQuestion = True
        
        if len(beforeAndAfter[0]) > 0 and not re.search(r"\.|\d", line[numI - 1]):
            print(line[numI - 1])
            partQuestion = True

        if inpArr.index(line) != 0:
            prevLine = inpArr[inpArr.index(line) - 1]
            print(prevLine)
            print(pnLineIMin)
            print(pnLineIMax)
            for j in range(pnLineIMin, pnLineIMax):
                print(str(j) + " " + str(prevLine[j]))
                if not re.search(r"\.|\d", prevLine[j]):
                    partQuestion = True

        if inpArr.index(line) != len(inpArr) - 1:
            nextLine = inpArr[inpArr.index(line) + 1]
            for j in range(pnLineIMin, pnLineIMax):
                print(str(j) + " " + str(nextLine[j]))
                if not re.search(r"\.|\d", nextLine[j]):
                    partQuestion = True
        
        if partQuestion:
            sum += int(num)
        
        print(str(num) + " " + str(partQuestion))
        print('')
        """print("PART 1 SUM: " + str(sum))"""

print("PART 1 SUM: " + str(sum))
print('')