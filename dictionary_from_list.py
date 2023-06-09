list1=["a","b","c","d","e"]
list2=[1,2,3,4,5]
#it may be wrong
dict1={"list1":list1,"list2":list2}
print(dict1)


#another way
dict2={}
for i in range(len(list1)):
    dict2[list1[i]]=list2[i]
print(dict2)


#another way
dict3=dict((key,value) for key,value in zip(list1,list2))
print(dict3)