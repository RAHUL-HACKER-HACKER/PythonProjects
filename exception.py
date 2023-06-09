#exception handling

# try:

#     age=int(input("ente your age:"))
#     print(age)
# except ValueError:
#     print("wrong value of age is entered")

# print("end of progrem,return the program")


#next program
# try:

#     age=int(input("ente your age:"))
#     weight=float(input("enter your weight:"))
#     index=weight/age
#     print(index)
# except ZeroDivisionError:
#     print("age can not be zero")


# except ValueError:
#     print("wrong value are entered")

# print("end of progrem,return the program")

#next programm
# keys=["name","age","id","add"]
# value=["rahul",19,12345,"india"]
# d1=dict(zip(keys,value))
# print(d1)


#next programm
# keys=["name","age","id","add"]
# values=["rahul",19,12345,"india"]
# dist = {}
# for key in keys:
#     for value in values:
#         dist[key] = value
#         values.remove(value)
#         break  
# print(dist)

#create a dictionary and  extract required key from dict
# d1={"a":1,"b":2,"c":3,"d":4}
# d2={"e":5,"f":6,"g":7,"h":8}
# for i in range(0,len(dict)):
#     key, val = dict.items()[i]
#     print(key,val)


#next probramm
# print(d1)
# d3={**d1,**d2}
# print(d3)
# list=[]
# for key in d1.keys():
#     list.append(key)
    
# n=int(input("enter key index:"))
# print(list[n])

#next programm
sample={"a":1,"b":2,"c":3,"d":4}
print(sample)
keys=["a","d"]
# n=input("enter required key")
# keys.append(n)
output={k:sample[k] for k in keys}
print(output)