lower = int(input ("Enter the Lowest Range Value: "))  
upper = int(input ("Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for nos in range (lower, upper + 1):  
    if nos > 1:  
        for i in range (2, nos):  
            if (nos % i) == 0:  
                break  
        else:  
            print (nos)  