numofValues = int(input("Enter the number of values:  "))

maxValue = int(input("Enter the first value:  "))
for index in range (numofValues-1):
    nextValue = int(input("Enter the next value:  "))
    if nextValue > maxValue:
        maxValue = nextValue

print ("The largest value is:  {0}".format (maxValue))
    
        

# def findMinandMax(numList):
# 
#     if len(numList) == 1:
# 
#         return numList[0]
# 
#     else:
#     
#         return max(numList[0]) > Max(findMinandMax(numList[1:]))
#         return numList[0] < findMinandMax(numList[1:])
#     
# # numList = promptForList()
# # findMinandMax(numList)

# print(findMinandMax([1,5,4]))