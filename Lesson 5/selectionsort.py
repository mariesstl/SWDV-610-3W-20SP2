# Consider the following list of integers: [1,2,3,4,5,6,7,8,9,10].
# Show how this list is sorted by the following algorithms:
# selection sort


def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
                temp = alist[fillslot]
                alist[fillslot] = alist[positionOfMax]
                alist[positionOfMax] = temp

alist = [1,9,3,4,8,10,7,5,2,6]
selectionSort(alist)
print(alist)