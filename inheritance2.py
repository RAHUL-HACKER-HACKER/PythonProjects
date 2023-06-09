class Person:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def show(self):
        print("name=",self.name,"age=",self.age,"salary=",self.salary)
class Employee(Person):
    def __init__(self, name, age, salary,id):
        self.id=id
        
        super().__init__(name, age, salary)
    def show(self):
        print("student id =",self.id)

    #super().__init__("Abc",35,10000)
    #super(Person).__init__("Abc",35,10000)
    #pass

# obj=Person("rahul",20,30);
# obj.show()


e1=Employee("Abc",35,10000,1)
e1.show()
Person.show(e1)


# e1=Employee("Abc",35,10000,1)
# e1.show1()
# e1.show2()