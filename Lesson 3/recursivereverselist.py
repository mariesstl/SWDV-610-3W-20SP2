# Write a recursive function to reverse a list.

def reverseMyList(numList):
    reversedList = []
    if len(numList) == 1: #Base Case: Evaluate only one item.
        return numList #There is only one value in original list. So, only one value in the new list.
    else:
        reversedList = reverseMyList(numList[1:])
        reversedList.append(numList[0])
        return reversedList
#         reversedList = reversedList[0] + reversedList(numList[1:])

            
print(reverseMyList([5,4,3,2,1]))
