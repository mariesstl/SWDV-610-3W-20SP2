def getMinMax(list):
    listMax = list[0]
    listMin = list[0]
    print ("Pre loop, Min: {0}, Max: {1}".format(listMin, listMax))
    for i in range(len(list)):
        print ('list value:', list[i])                  
        if list[i] > listMax:
            listMax = list[i]
        if list [i] < listMin:
            listMin = list[i]
        print ("Max: {}".format(listMax))
        print ("Min: {}".format(listMin))
        print ("loop, {0} Min: {1}, Max: {2}".format(i,listMin, listMax))
    print ("FINAL Min: {0}, Max: {1}".format(listMin, listMax))
            
print(getMinMax([1.4,5,4,3,8,9,30,-1.9,7,99, 34, -5]))