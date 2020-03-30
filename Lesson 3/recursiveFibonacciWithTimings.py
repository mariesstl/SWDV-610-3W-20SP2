# Python program to display the Fibonacci sequence up to n-th term using recursive functions
import time

def recur_fibo(n):

    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

# Change this value for a different result
nterms = 30

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    start = time.time()
    for i in range(nterms):
        recur_fibo(i)
    end = time.time()
    print ("time taken:{0:>10.7f}".format(end-start))