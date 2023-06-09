
from tracemalloc import stop
from xmlrpc.client import boolean



x=boolean(input("enter true/false :"))
while (x):
    n=input("enter start or stop :")
    if n=="start":
        print("car is moving")
    
    elif n=="stop":

        print("car is stoped")

    x=input("enter true/false :")


