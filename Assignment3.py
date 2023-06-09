list=[2,4,8,10,40,50]
n=int(input("enter any integer:"))
temp=0
for i in list:
    if n==i:
        temp+=1
if temp>0:
    print("success")

else:
    print("failure")


