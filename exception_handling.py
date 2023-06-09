from warnings import catch_warnings


def divide():
    n=int(input("enter dividend:"))
    m=int(input("enter divisor enteger:"))
    try:
        div=n/m
        print("quotient=",div)
    except ZeroDivisionError:
        print("we can not divide by zero")

    finally:
        print("may be other problem")

divide()
    
