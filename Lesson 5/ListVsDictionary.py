# What is the difference between a list and a dictionary?
# Dictionaries differ from lists in that you can access items in a dictionary
# by a key rather than a position. Duplicate keys are not allowed. Can have a default key.
# Lists are ordered. Dictionaries are key value pairs.
# Build a script that utilizes at least one list and one dictionary.

contactsDict = {}
scoresList = []

def ContactsDict():
    contactsDict = {'Jane Adams':'314.896.4444'}
    print('Print Dictionary',contactsDict)
    contactsDict.update({'Ronna James': '505.444.2222'})
    print("After Addition:",contactsDict)
    #Find Value - By Key
    print("Jane's Phone Number: ",contactsDict.get('Jane Adams'))
    #Update a value
    contactsDict.update({'Jane Adams': '314.249.5555', 'Fred Smith': '202.334.5555', 'Lisa Wyre': '313.555.2222'})
    print("Jane's New Phone Number: ",contactsDict.get('Jane Adams'))
    #Remove a value
    contactsDict.pop('Fred Smith')
    print("After Deletion:",contactsDict)
    #check for item in dictionary
    print('Is Andrea Lee in there?','Andrea Lee' in contactsDict)
    print('Is Lisa Wyre in there?','Lisa Wyre' in contactsDict)
    #List names
    print ('Keys: ',contactsDict.keys())    
    #List values
    print ('Values: ',contactsDict.values())    
    #List Items
    print ('Items: ', contactsDict.items())
    #Retrieve a value with a key
    print(contactsDict.get('Fred Smith'))
    print(contactsDict.get('Lisa Wyre'))
    #Copy Dictionary to New Dictionary
    newContactsDict = contactsDict.copy()
    #Clear Dictionary
    contactsDict.clear()
    print('Old Dictionary:',contactsDict)
    print('New Dictionary:',newContactsDict)
        
def GradesList():
    gradesList = [90,89,95,75,99,55,95,3,6,76]
    print('Grade List:',gradesList)
    #sort
    gradesList.sort()
    print('Sorted',gradesList)
    #reverse
    gradesList.reverse()
    print('Reversed',gradesList)
    #Get values by Positon - index, Slice
    print('By Index',gradesList[4])    
    print('By Slice',gradesList[5:8])
    print('Count 99:',gradesList.count(95))    
    #Multiple values in the list
    print("Multiply values X 2",[x* 2 for x in gradesList])
    #Multiply the List itself
#     gradesList = gradesList*3
    print("Multiply the list itself by 3",gradesList*3)
    
def Main():
    ContactsDict()
    GradesList()   

Main()

