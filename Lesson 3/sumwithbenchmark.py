import time

def sumofNumber(number):
    start = time.time()
    
    mySum = 0
    for i in range (1, number+1):
        mySum = mySum + 1
   
    end = time.time()
    
    return mySum,end-start

for i in range(5):
    print("Sum is %d required:%10.7f seconds:"%sumofNumber(100000))
