import re

file1 = open("input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n")
file1.close()
finalArr = []

def wordToNum(word):
    if word == "one":
        return 1
    elif word == "two":
        return 2
    elif word == "three":
        return 3
    elif word == "four":
        return 4
    elif word == "five":
        return 5
    elif word == "six":
        return 6
    elif word == "seven":
        return 7
    elif word == "eight":
        return 8
    elif word == "nine":
        return 9

for i in inpArr:
    first = "".join(re.findall(r"(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(\d)", i)[0])
    last = ("".join(re.findall(r"(eno)|(owt)|(eerht)|(ruof)|(evif)|(xis)|(neves)|(thgie)|(enin)|(\d)", i[::-1])[0]))[::-1]
    if re.search(r"[A-z]", first):
        first = str(wordToNum(first))
    if re.search(r"[A-z]", last):
        last = str(wordToNum(last))
    
    finalI = first + last
    finalArr.append(int(finalI))
    """print(finalI)"""

sum = 0
for j in finalArr:
    sum += j

print(sum)