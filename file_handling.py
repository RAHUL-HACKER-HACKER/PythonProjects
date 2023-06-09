
import os
#use for creat file
# file=open("abc.txt","x")
# file.close()


file=open("rahul.txt","w")
file.write("hello my name is rahul kumar.\n I am from america.")
file.write("\n America is beautyful contry. ")
file.close()
#or use append fn for adding sentence without overlaping
file=open("rahul.txt","a")
file.write("And it is neat and clean")
file.close()

file=open("rahul.txt","r")

t1=file.read()
#t1=file.read(5) ->use for slicing

# t1=file.readlines() ->use for print a line
# for i in t1:
#     print(i,end=" ")
 
print(t1)

file.close()

#remove new file
file2=open("temp.txt","x")#created new file
file2.close()
if os.path.exists("temp.txt"):
    os.remove("temp.txt")
    print("file remove successfilly")

else:
    print("file does not exist")

