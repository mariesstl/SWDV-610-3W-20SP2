'''
is_multiple(n, m), that takes two integer values and returns True
is n is a multiple of m, that is, n = mi for some integer i, and False otherwise.
'''

def is_multiple(integerMultiple, integer):
    integerMultiple = int(input("Enter an integer to evaluate for a multiple: "))
    integer = int(input("Enter an integer to evaluate as a multiple of the previous integer: "))
    
    if integerMultiple % integer == 0:
        print(True)
    else:
        print(False)
        
def main():
    is_multiple(15,5)

main()