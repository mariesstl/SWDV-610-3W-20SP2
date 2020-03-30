'''
A common punishment for school children is to write out a sentence multiple times.
Write a Python stand-alone program that will write the following sentence one hundred times:
I will never spam my friends again.
'''

def punishment():
    counter = 0 #Keeps track of how many times the sentence is repeated.
    while counter < 100:
        print("I will never spam my friends again.")
        counter += 1 #Add one to the counter each time the loop continues

def main():
    punishment()
    
main()