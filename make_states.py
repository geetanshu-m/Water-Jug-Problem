states = {}
A = 4
B = 3
final_A = 2

def fillA(x, y):
    x = A
def fillB(x, y):
    y = B
def pourBtoA(x, y):
    if x + y <= A:
        x = x + y
        y = 0
    else:
        temp = A - x
        y = y - temp
        x = A
def pourAtoB(x, y):
    if x + y <= B:
        x = 0
        y = x + y
    else:
        temp = B - y
        x = x - temp
        y = A
def emptyA(x, y):
    x=0
def emptyB(x, y):
    y=0