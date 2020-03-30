# Write a recursive function to reverse a list.

def reverseMyList(numList):
    reversedList = []
    if len(numList) == 1: #Base Case: Evaluate only one item.
        return numList #There is only one value in original list. So, only one value in the new list.
    else:
        reversedList = reverseMyList(numList[1:])#Separate out the left-most item and then evaluate...all the way down.
        reversedList.append(numList[0])# append the item to the new list in reversed order.
        return reversedList
            
print(reverseMyList([5,4,3,2,1]))
