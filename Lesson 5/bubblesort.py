# Consider the following list of integers: [1,2,3,4,5,6,7,8,9,10].
# Show how this list is sorted by the following algorithms:
# bubble sort

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def main():
    alist = [1,9,3,4,8,10,7,5,2,6]
    bubbleSort(alist)
    print(alist)
    
main()
