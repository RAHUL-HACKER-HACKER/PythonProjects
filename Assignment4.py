


n=int(input("enter no of student"))

class Student:
    def __init__(self,name,reg,mark):
        self.name=name
        self.reg=reg
        self.mark=mark


    def disp(self):
        print("name:",self.name)
        print("registration number:",self.reg)
        print("mark:",self.mark)

for i in range(n):
    name=input("enter student name:")          
    reg=input("enter student reg:")          
    mark=input("enter student mark:")  
    s1=Student(name,reg,mark) 
    s1.disp() 

    
   