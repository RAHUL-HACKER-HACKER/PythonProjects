class A(object):
    def __init__(self):
        print("Entering A")
        

class B(object):
    def __init__(self):
        print("Entering B")
        
class C(A, B):
    def __init__(self):
        print("Entering C")
        A.__init__(self)
        B.__init__(self)
        

obj=C()