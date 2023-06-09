#regular expression
#r=row(mean cover all row)
import re
str="ACB BCAAAAC Eara and Rahul are good friend.now going to invest 20 rupies ID 300 3.running"
name=re.findall(r'[A-Z][a-z]*',str)
num=re.findall('\d{2}',str)
end=re.findall('ing$',str)

print(name)
print(num)
print(end)
print("new code")
sp=re.findall(r'[A-Z][a-z]...',str)
print(sp)
sp1=re.findall(r'[a-z]*ing$',str)
print(sp1)
print("new code")
sp2=re.findall(r'\d[3,0,1]',str)
print(sp2)
#return boolean
search1=re.search("Rahul",str)
print(search1)
#return list
search2=re.findall("Rahul",str)
print(search2)
print("new code")
sp3=re.findall(r'[RABC][a-z]*',str)
print(sp3)

sp4=re.findall(r'[0-9]*',str)
print(sp4)



sp5=re.findall(r'\d',str)
print(sp5)




