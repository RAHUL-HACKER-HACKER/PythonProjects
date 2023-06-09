#abstraction
from abc import ABC, abstractmethod
class pokeman(ABC):
    def __init__(self,name,attack_type):
        self.name=name
        self.attack_type=attack_type
        @abstractmethod
        def attack(self):
            pass
class pikachu(pokeman):
    myattack="fire"
    def __init__(self,name,attack_type,symbol):
        super().__init__(name,attack_type)
        self.symbol=symbol
    def attack(self):
        return self.myattack

p1=pikachu("google",'fire',"sun")
p1.attack()

print(p1.name)

