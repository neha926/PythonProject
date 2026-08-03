def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

while True:
    num1=int(input("Enter First Value..."))
    num2=int(input("Enter Second Value..."))
    print("Enter Operator:\
    1:Addition \
    2:Subtraction \
    3:Multiplication \
    4:Division\
    5:Exit"
    )
    operator=input("What operation you want to perform ..?")
    if operator=="1":
        print(add(num1,num2))
    elif operator=="2":
        print(sub(num1,num2))
    elif operator=="3":
        print(mul(num1,num2))
    elif operator=="4":
        print(div(num1,num2))
    elif operator=="5":
        break;
    else:
        print("Invalid Key")


    

