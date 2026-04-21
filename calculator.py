
def add(a,b):
    print("ADDITION:",a+b)
def sub(a,b):
    print("SUBSTRACTION:",a-b)
def mul(a,b):
    print("MULTIPLICATION:",a*b)
def div(a,b):
    print("DIVISION:",a/b)
def floor_div(a,b):
    print("FLOOR DIVISION:",a//b)
def exponent(a,b):
    print("EXPONENTIAL:",a**b)
def less_than(a,b):
    print("LESS THAN OPERATOR:",a<b)
def greater_than(a,b):
    print("GREATER THAN OPERATOR:",a<b)
while True:
    print("WELCOME TO OUR SIMPLE CALCULATOR")
    print("1.ADD")
    print("2.SUB")
    print("3.MUL")
    print("4.DIV")
    print("5.FLOOR DIVISION")
    print("6.EXPONENTIAL")
    print("7.LESS_THAN OPERATOR")
    print("8.GREATER_THAN OPERATOR")
    print("9.EXIT")
    choice=int(input("Enter your choice:"))
    a = int(input("Enter your first number:"))
    b = int(input("Enter your second number:"))
    if choice==1:
        add(a,b)
    elif choice==2:
        sub(a,b)
    elif choice==3:
        mul(a,b)
    elif choice==4:
        div(a,b)
    elif choice==5:
        floor_div(a,b)
    elif choice==6:
        exponent(a,b)
    elif choice==7:
        less_than(a,b)
    elif choice==8:
        greater_than(a,b)
    elif choice==9:
        break
print("THANK YOU FOR VISITING HERE............")






