import time
def fibonacciloop(number):
    start = time.time()
    print("fibonacci evaluation of: {0}".format(numbertoevaluate))
    if number == 0:
        return [0]
    if number == 1:
        return [0,1]

    sequence = [0, 1]#Always starts with 0 and 1
    
    for i in range(2,number+1):
       sequence.append(sequence[i-1] + sequence[i-2])#Add the previous two elements together, then append their sum to the list.
    
#     print("Fibonacci Sequence: ", sequence)
    end = time.time()
    return sequence,end-start
    

numbertoevaluate = 10000
# fibonacciloop(numbertoevaluate)


for i in range(5):
    print("Fibonacci required:%10.7f seconds:"%fibonacciloop(numbertoevaluate)[1])
