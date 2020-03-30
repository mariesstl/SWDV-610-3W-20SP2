# Write a short recursive Python function that finds the minimum
# and maximum values in a sequence without using any loops.

def findMinandMax(numList):
    min = numList[0]
    max = numList[0]
    if len(numList) == 1: #Base Case: Evaluate only one item.
        return min, max #There is only one value. Making it min and max.
    else:
        newMin,newMax = findMinandMax(numList[1:]) #Each call will separate out the left-most value.
        if newMin < min:
            min = newMin
        if newMax > max:
            max = newMax
            
        return min, max 

            
print(findMinandMax([1,5,4,2]))
            
