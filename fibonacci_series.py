n=int(input("enter integer :"))

a=0
b=1
count=0
while count<n :
    print(a,end=" ")
    a,b=b,a+b
    count=count+1
    #print()
    
