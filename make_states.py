class make_states:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def fillA(self, x, y):
        x = self.A
        return x,y

    def fillB(self, x, y):
        y = self.B
        return x,y

    def pourBtoA(self, x, y):
        if x + y <= self.A:
            x = x + y
            y = 0
        else:
            temp = self.A - x
            y = y - temp
            x = self.A
        return x,y

    def pourAtoB(self, x, y):
        if x + y <= self.B:
            x = 0
            y = x + y
        else:
            temp = self.B - y
            x = x - temp
            y = self.B
        return x,y

    def emptyA(self, x, y):
        x=0
        return x,y

    def emptyB(self, x, y):
        y=0
        return x,y