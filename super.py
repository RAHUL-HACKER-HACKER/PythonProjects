class Person:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def disp1(self):
        print("name:",self.name)
        print("age:",self.age)
        print("slary:",self.salary)


class Employee(Person):
    def __init__(self,name,age,salary,bonus):
        super().__init__(name,age,salary)
        self.bonus=bonus

    def disp2(self):
        print("bonus:",self.bonus)


e1=Employee("rahul",18,1000000,1000)
e1.disp1()
e1.disp2()


#next line
class Teacher:
    def __init__(self,name,dept,salary):
        self.name=name
        self.dept=dept
        self.salary=salary
    def show_details(self):
        print(f'Name: {self.name} dept: {self.dept} salary:{self.salary}')

t=Teacher("hari","scse",1000000)
t.show_details()

#movies website
#use file managment
#show movie_name ,movie_title,movie_photo(poster),movie_trailer,movie_story-line
movie1=
movie2=
list=[movie1,movie2,...]
class movies:
    def __init__(self):