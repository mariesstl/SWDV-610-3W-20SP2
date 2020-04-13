x = {} #my dictionary
for i in x:
    color = "#%06x" % random.randint(0, 0xFFFFFF)
    x[i] = [x[i], color]
print (x)