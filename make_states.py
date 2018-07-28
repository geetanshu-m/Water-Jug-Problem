states = {}
A = 4
B = 3
final_A = 2

def fillA(x, y):
    x = A
    return x,y

def fillB(x, y):
    y = B
    return x,y

def pourBtoA(x, y):
    if x + y <= A:
        x = x + y
        y = 0
    else:
        temp = A - x
        y = y - temp
        x = A
    return x,y

def pourAtoB(x, y):
    if x + y <= B:
        x = 0
        y = x + y
    else:
        temp = B - y
        x = x - temp
        y = B
    return x,y

def emptyA(x, y):
    x=0
    return x,y

def emptyB(x, y):
    y=0
    return x,y