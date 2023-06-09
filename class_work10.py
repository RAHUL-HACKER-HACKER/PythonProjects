#use pipe

# from pipe import where,select

#map
#filter

# filter(lambda x:x%2==0)
# Iterable
   

# l1=[1,2,3,4,5]
 

#Write Clean Python Code Using Pipe

# l2=l1|where(lambda x:x**2)
# print(l2)

#reference(https://towardsdatascience.com/write-clean-python-code-using-pipes-1239a0f3abf5)


#reference(https://towardsdatascience.com/write-clean-python-code-using-pipes-1239a0f3abf5)

from pipe import where,select,dedup
l1 = [1, 2, 3, 4, 5,6,7]

l2 = list(l1 | select(lambda x:x%2==0))#it does operation
print(l2)
l3 = list(l1 | where(lambda x:x%2==0))#it does filter
print(l3)
l7 = list(l1 | select(lambda x:x**2)|where(lambda x:x%2==0))
print(l7)

#OR both are same
l4=list(map(lambda x:x%2==0,l1))
print(l4)
l5=list(filter(lambda x:x%2==0,l1))
print(l5)
l6=list(map(lambda y:y**2,filter(lambda y:y%2==0,l1)))
print(l6)





# pip install pipe
# from pipe import select, where, dedup


arr = [1,2,3,4,5,4,3,2,1,1,1]

res = list(arr
    | dedup					  # remove duplicates -> [1,2,3,4,5]
    | where(lambda e: e%2 == 0)  # filter for even numbers -> [2,4]
    | select(lambda e: e * 2)    # double all numbers -> [4,8]
)