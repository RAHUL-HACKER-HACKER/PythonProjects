import time


def tap(water):
    
    if (water=="hot" or water=="cold" or water=="chill"):
        dict={"hot":"red","cold":"green","chill":"blue"}
        a1=input(f"please fit your bottle in {dict[water]} nozzle of tap and click(yes/no) :")
        if a1=="yes":
            print(f"-----wait------ (now {water} water is being filled)")
            time.sleep(5)
            print("water has been filled you can remove your bottle")
        else:
            i=3
            while i>0: 
                print(f"opps! only {i} attempt left")
                b1=input(f"Again fit your bottle properly in {dict[water]} nozzle of tap and click(yes/no) :")
                i-=1  
                if(b1=="yes"):
                    print("-----wait------ (now {water} water is being filled)")
                    time.sleep(5)
                    print("water has been filled you can remove your bottle")
                    break 
    
    

while True:
    n=input("you want to filling water then enter(yes/no):")
    if n=="yes":
        while True:

            water1=input("which type of water you want please select from given options(hot,cold,chill:")
            if (water1=="hot" or water1=="cold" or water1=="chill"):
                tap(water1)
                break
            else:
                print("----warning-----please enter proper input")
        
    elif n=="no":
        print("------thanks for visit-------")
        break

    else:
        print("----warning-----please enter proper input")

      
      
        
