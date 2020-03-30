# function to reverse a list.

def reverseList(numList):
    reversedList = []
    lengthofNumList = len(numList)-1
    print("given list length: ", lengthofNumList)
    for i in range(0,lengthofNumList+1):
        print('i',i)
        reversedList.append((numList[lengthofNumList-i]))  
    print(reversedList)
         
print(reverseList([5,4,3,2,1]))





