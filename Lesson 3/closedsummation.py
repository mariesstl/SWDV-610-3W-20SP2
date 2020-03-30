def sumofNumber(number):
    return(number*(number+1))/2

for i in range(5):
    print("Sum is %d required:%10.7f seconds:"%sumofNumber(100000))

