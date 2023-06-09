a="rahul"
b="kumar"
c=10
d=5

#print(c<>d)



# __le__
# __lt__
# __add__
class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):

        return("{0},{1}").format(self.x,self.y)

    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return point(x,y)
    def __sub__(self,other):
        x=self.x-other.x
        y=self.y-other.y
        return point(x,y)
        
    def __mul__(self,other):
        x=self.x*other.x
        y=self.y*other.y
        return point(x,y)

    def __le__(self,other):
        x=self.x<=other.x
        y=self.y<=other.y
        return point(x,y)
    def __com__(self,other):
        x=self.x==other.x
        y=self.y==other.y
        return point(x,y)
   


p1=point(10,20)
p2=point(20,30)
print(p1+p2)
print(p1.__add__(p2))
print(p1.__sub__(p2))
print(p1.__mul__(p2))
print(p1.__le__(p2))
print(p1.__com__(p2))
#print(p1+p2)


class employee:
    def __init__(self,name,base_pay):
        self.name=name
        self.base_pay=base_pay

    def get_pay(self):
        return(self.base_pay)

class salesEmployee:
    
    def __init__(self,name,base_pay,sales_incentive):
        self.name=name
        self.base_pay=base_pay
        self.sales_incentive=sales_incentive
    def get_pay(self):
        return(self.base_pay+self.sales_incentive)
        
        


