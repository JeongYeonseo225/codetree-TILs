def f(a,b):
    if a<b:
        return a+10,2*b
    else:
        return 2*a, b+10
        
a,b =tuple(map(int,input().split()))

a1,b1=f(a,b)
print(a1,b1)