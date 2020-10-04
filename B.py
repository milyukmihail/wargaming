import sys

args = sys.stdin.readlines(2)

gold = int(args[0][0])

cost = args[1].split()

costWithNumb = {
    1 : cost[0], 2 : cost[1], 3 : cost[2],
    4 : cost[3], 5 : cost[4], 6 : cost[5],
    7 : cost[6], 8 : cost[7], 9 : cost[8]}

dictAfterFor = {}

#Ubrali cifry s bolshoy stoimostiy
for key in costWithNumb:
    if int(costWithNumb[key]) <= gold:
        dictAfterFor[key] = costWithNumb[key] # All right


def CheckGoldTwo(gold, dictAfterFor): #If not gold for 1 char
    if hasattr(dictAfterFor, '__iter__'):
        for key in dictAfterFor:
            for key1 in dictAfterFor:
                if int(dictAfterFor[key]) + int(dictAfterFor[key1]) <= gold:
                    return True
                else:
                    return False
    else:
        return False

def CheckGold(gold, dictAfterFor):
    if hasattr(dictAfterFor, '__iter__'):
        for key in dictAfterFor:
            if int(dictAfterFor[key]) <= gold:
                return True
            else:
                return False
    else:
        return False


#K kazhdoy cifre cazhduyu dlya naibolshego chisla
def MaxNumber(dictAfterFor, gold, maxLength):
    if CheckGoldTwo(gold, dictAfterFor):#If have golda for 2 char, then go
        maxLengthTwoNumb = 0
        keys = dictAfterFor.keys()
        for key in dictAfterFor:
            for key1 in dictAfterFor:
                if int(dictAfterFor[key]) + int(dictAfterFor[key1]) <= gold and int(str(min(keys)) + str(min(keys))) >= int(str(key) + str(key1)):
                    maxLengthTwoNumb = str(key) + str(key1)
        maxLength = str(maxLength) + str(maxLengthTwoNumb)
        maxLengthForGold = sum(map(int, maxLength))#Summ numbers
        gold = gold - maxLengthForGold#New gold after minus summ
        if CheckGoldTwo(gold, dictAfterFor):
            return MaxNumber(dictAfterFor, gold, maxLength)
    if CheckGold(gold, dictAfterFor):#If have golda for 1 char, then
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

sys.stdout.write(str(value))

