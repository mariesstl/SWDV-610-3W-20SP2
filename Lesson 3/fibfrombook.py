def fibanacci():
    a=0
    b=1
    while true:
        yield a
        future = a + b
        a=b
        b = future
        
fibanacci()