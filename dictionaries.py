# dict={"name":"rahul","age":20,"reg":10063}
# print("name=",dict["name"])
# print("age=",dict["age"])
# print("reg",dict["reg"])
# print(type(dict))

# dict["add"]="india"
# print(dict)
# print("add" in dict)
# print("add" not in dict)
# del dict["reg"]
# print(dict)
# list(dict)
# print(dict)
# print(sorted(dict))


dict={"a":1,"b":2,"c":3,"d":4}
for i in dict:
    print(i,end="")
    
print()
for i in dict:
    
    print(dict[i],end="")
print()
for i in dict.values():
    print(i,end="")