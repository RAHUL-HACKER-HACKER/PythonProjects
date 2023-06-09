# class Student:
#     def __init__(self,name,reg):
#         self.name=name
#         self.reg=reg
        
        
#     def disp(self,salary):
#         self.salary=salary
#         print("salary of student:",self.salary)
#         print("name of student:",self.name,self.reg)

# class deri(Student):
#     def __init__(self,add,name,reg):
#         self.add=add
#         super().__init__(name,reg)
        



#     def disp2(self):
#         print("add of student:",self.add)


# obj2=deri("jahanabad",'anand',10063)
# obj2.name="anand"
# obj2.disp(200000)

# obj2.disp2()

#prime no checking
# n=int(input("enter any interger:"))
# no_prime=False
# for i in range(2,n):
#     if n%i==0:
#         no_prime=True
#         break
# if no_prime:
#     print(n," is not prime number")
# else:
#     print(n," is a prime no")


#print prime no bet range
# n=int(input("enter lower value:"))
# m=int(input("enter upper value:"))

# for i in range(n,m+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=",")

#another way to print prime no bet range
# n=int(input("enter lower value:"))
# m=int(input("enter upper value:"))

# for i in range(n,m+1):
#     temp=True
#     for j in range(2,i):
#         if i%j==0:
#             temp=False
#             break
#     if temp:
#         print(i,end=",")

#fibonacci series
# n=int(input("enter fibo series size:"))
# a,b=0,1
# temp=0
# for i in range(n):
   
#     print(a,end=",")
#     temp=b
#     b=a+b
#     a=temp

#checking armstrong number
# m=int(input("enter any integer:"))
# n=m
# temp=0
# while n>0:
#     digit=n%10
#     temp+=digit**3
#     n=n//10

# if temp==m:
#     print(m," is a armstrong number")
# else:
#     print(m," is not a armstrong number")

list=[]
for i in range(3):
    list1=[]
    for j in range(3):
        list1.append(j)
    list.append(list1)
print(list)
for i in range(3):
    for j in range(3):
        print(list[i][j],end=" ")
    print()

     


    
    