#regular expressions
from ast import pattern
import re
pattern='^a....s$'
test_string='abyss'
result=re.match(pattern,test_string)
if result :
    print("search successful.")
else:
    print("search unsuccessful")

#findall
s="the rain is spain .this is a python program"
pattern="program\Z"
result=re.findall(pattern,s)
print(result)

#next program
pin=input("enter pin:")
pattern="[1-3][4-6][7-9][0]"
#x=re.match('\d{4}\z',pin)
x=re.match(pattern,pin)
if x:
    print('valid pin')
else:
    print("invalid pin")



#next program
# import re
 
# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
# def check(email):
 
    
#     if(re.fullmatch(regex, email)):
#         print("Valid Email")
 
#     else:
#         print("Invalid Email")
 
# if __name__ == '__main__':
 
    
#     email = "ankitrai326@gmail.com"
 
    
#     check(email)
 
#     email = "my.ownsite@our-earth.org"
#     check(email)
 
#     email = "ankitrai326.com"
#     check(email)

    #next programm
    mail=input("enter mail:")
    pattern="[a-z].*@|gmail.com"
    x=re.match(pattern,mail)
    if x:
        print("vaild email id")
    else:
        print("invailid eamil id")
    
