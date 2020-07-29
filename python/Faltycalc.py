def calc():
    if operate=="+":
        c=a+b
    elif operate=="-":
        c=a-b
    elif operate=="*I":
        c=a*b
    elif operate=="/":
        c=a/b
    return c



n=18
while True:

    print("     Calculator :-    ")
    operate = input("Enter the operation sign you want to do :- ")
    a=int(input("Enter First Value :- "))
    b=int(input("Enter First Value :- "))
    if operate=="+":
        c=a+b
    elif operate=="-":
        c=a-b
    elif operate=="*I":
        c=a*b
    elif operate=="/":
        c=a/b
    if a==45 and operate=="*" and b==3:
        c=555
    elif a==56 and operate=="+" and b==0:
        c=77
    elif a==56 and operate=="/" and b==6:
        c=4

    print("Result of "+str(a)+str(operate)+str(b)+" is : "+str(c))
