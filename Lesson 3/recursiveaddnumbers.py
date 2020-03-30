def listsum(numList):

    if len(numList) == 1:

        return numList[0]

    else:

        return numList[0] + listsum(numList[1:])

print(listsum([1,5,4,2,6,7.6]))
