def f(a,b):
    if a<b:
        return 2*a, b+25
    else:
        return a+25, 2*b

a,b=tuple(map(int,input().split()))
a1,b1=f(a,b)
print(a1,b1)