import sys

gold = int(input())
cost = input()
cost = cost.split()

costWithNumb = {
    1 : cost[0], 2 : cost[1], 3 : cost[2],
    4 : cost[3], 5 : cost[4], 6 : cost[5],
    7 : cost[6], 8 : cost[7], 9 : cost[8]}

dictAfterFor = {}

for key in costWithNumb:
    if int(costWithNumb[key]) <= gold:
        dictAfterFor[key] = costWithNumb[key]


def CheckGoldTwo(gold, dictAfterFor):
    k = 0
    if hasattr(dictAfterFor, '__iter__'):
        for key in dictAfterFor:
            for key1 in dictAfterFor:
                if (int(dictAfterFor[key]) + int(dictAfterFor[key1])) <= gold:
                    k = 1
        if k == 1:
            return True
        else:
            return False
    else:
        return False

def CheckGold(gold, dictAfterFor):
    k = 0
    if hasattr(dictAfterFor, '__iter__'):
        for key in dictAfterFor:
            if int(dictAfterFor[key]) <= gold:
                k = 1
        if k == 1:
            return True
        else:
            return False
    else:
        return False


def MaxNumber(dictAfterFor, gold, maxLength):
    if CheckGoldTwo(gold, dictAfterFor):
        maxLengthTwoNumb = 0
        keys = dictAfterFor.keys()
        for key in dictAfterFor:
            for key1 in dictAfterFor:
                if int(dictAfterFor[key]) + int(dictAfterFor[key1]) <= gold and int(str(min(keys)) + str(min(keys))) <= int(str(key) + str(key1)):
                    maxLengthTwoNumb = str(key) + str(key1)
        maxLength = str(maxLength) + str(maxLengthTwoNumb)
        maxLengthForGold = sum(map(int, maxLength))
        gold = gold - maxLengthForGold
        if CheckGoldTwo(gold, dictAfterFor):
            return MaxNumber(dictAfterFor, gold, maxLength)
    if CheckGold(gold, dictAfterFor):
        maxElForCurrentGold = 0
        for key in dictAfterFor:
            if int(dictAfterFor[key]) <= gold and maxElForCurrentGold <= int(key):
                maxElForCurrentGold = key
        maxLength = str(maxLength) + str(maxElForCurrentGold)
        maxLength = int(maxLength)
        return str(maxLength)
    else:
        maxLength = int(maxLength)
        return str(maxLength)


value = MaxNumber(dictAfterFor, gold, 0)

if value == '0':
    sys.stdout.write(str(-1))
else:
    sys.stdout.write(str(value))

