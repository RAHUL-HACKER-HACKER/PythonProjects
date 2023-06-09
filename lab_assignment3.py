matrix1=[]
n=int(input("Enter squre matrix1 size: "))         
print("Enter the element of matrix1:")
for i in range(n): 
    row=[]                                     
    for j in range(n):
        temp=int(input("enter element:"))
        row.append(temp)         
    matrix1.append(row)                      
print(matrix1)

                                     
matrix2=[]
n=int(input("Enter squre matrix2 size: "))        

print("Enter the element ::>")
for i in range (n): 
    row=[]                                     
    for j in range(n):
        temp=int(input("enter element:"))
        row.append(temp)          
    matrix2.append(row)                      
print(matrix2)

                                        
result = [[0]*n]*n
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])): 
        for k in range(len(matrix2)): 
            result[i][j] += matrix1[i][k] * matrix2[k][j] 

print("multiplication of two Matrix Is :")
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):  
         print(result[i][j],end=" ")
    print()
 
