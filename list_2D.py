rows, cols = (5, 5)
arr=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(j)
    arr.append(col)
print(arr)


#other way
row=3
col=5
list=[[0]*col]*row
list[1][1]=1
print(list)

#other way
row=3
col=5
list=[[0 for i in range(col)] for j in range(row)]
list[1][1]=1
print(list)


