class my_class:
    def method1(self):
        return "Hello World"
    def method2(a, methodToRun):
        result = methodToRun
        return result+a.method1()

obj = my_class()
#method1 is passed as an argument
print(obj.method2("hello"))