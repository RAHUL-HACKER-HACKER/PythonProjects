class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, obj):
        self.x = obj.x + self.x
        self.y=obj.y+self.y
        print(self.x,self.y)


A = Position(1, 1)
B = Position(2, 3)
A.add(B)


class computer:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __str__(self):
        return("{0},{1}").format(self.name,self.price)

    def getprice(self):
        return self.price
    def __it__(self,other):
        if(self.getprice()<other.getprice()):
            return other
        else:
            return self

c1=computer("msi",70000)
c2=computer("dell",100000)
print(c1<c2)
