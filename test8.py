from multiprocessing.sharedctypes import Value


keys=['a','b','c','d','e']
values=[1,2,3,4,5]

dicts=dict((key,value) for key, value in zip(keys,values))
print(dicts)
print(type(dicts))


for i,j in keys,values:
    #d[keys[i]]=values[i]
    print(i,",",j)





