def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiple(a,b):
    return a*b

def divide(a,b):
    return a//b

a,o,c=input().split()
a=int(a)
c=int(c)
if o =='+':
    print(f"{a} {o} {c} = {plus(a,c)}")
elif o=='-':
    print(f"{a} {o} {c} = {minus(a,c)}")
elif o=='*':
    print(f"{a} {o} {c} = {multiple(a,c)}")
elif o=='/':
    print(f"{a} {o} {c} = {divide(a,c)}")
else:
    print("False")