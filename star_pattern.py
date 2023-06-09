#star print using while loop 
# n=int(input("inter pattern size:"))

# i=1
# while i<=n:
    
    
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1



#star print using for loop
n=int(input("enter pattern size:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()


