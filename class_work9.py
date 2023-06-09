f=open("text.txt",mode="w")
f.write("hello rahul")

f.close()
f=open("text.txt","r")
str=f.read()
print(str)

f.close()

try :
    f=open("text.txt","w")
    f.close()
except FileNotFoundError:
    print("file does not exists")
finally:
    print("program executed")

#or we can write
with open('text.txt','w') as f:
    pass

#new program
f=open("text.txt",'w')
f.write("\nadd new word")
#print(f.tell())
# print(f.seek(4))
# print(f.read())
f.close()
f=open('text.txt','r')
print(f.readlines())#print line in list


