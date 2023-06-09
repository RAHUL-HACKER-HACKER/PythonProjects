


# class point:
#     x=0;
#     def move(self):
#         print("move it")
#     def draw(self):
#         print("draw it")

# obj=point()
# obj.move()
# obj.draw()
# print(obj.x)
# obj.y=100
# obj.z=200
# print(y)

#next program
# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

# obj=point(100,300)
# print(obj.x)
# print(obj.y)


# class student:
#     def __init__(self,id,name):
#         self.name=name
#         self.id=id
    
#     def exam(self):
        
#         print("student id:",self.id)
#         print("student name:",self.name)

# obj=student(2022,"rahul")
# obj.exam()
list=[]
for i in range(0,2):
    for j in range(0,2):
        n=int(input("enter point",i,"value",j,":"))
        list.append(n)
dist=(((list[0]+list[1])**2)+((list[2]+list[3])**2))**1/2
    

    

