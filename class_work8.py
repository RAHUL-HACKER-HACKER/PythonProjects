
#exception and error handling



#while True print("rahul")
#print(1/0)

#print(4*spam*3)

# n=int(input("enter a integer"))
# print(n)


#handling exception
#try ,except,raise,finaly
while True:
    try:
        age=int(input("please enter the age:"))
        weight=float(input("enter the weight:"))
        index=weight/age
        print(index)
        #break
    except ValueError:
        print("wrong value of age is entered")

    except ZeroDivisionError:
        print("age can not be zero")

    finally:
        print("end of programm " )