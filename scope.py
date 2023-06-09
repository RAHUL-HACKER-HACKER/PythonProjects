#golobal scope
x=0

def outer():
    #enclosed scope
    x=1
    print(x)
    def inner():
        #local scope
        print(x)
        x=2

print(x)
outer()
#outer.inner()



