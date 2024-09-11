def f(a,b):
    a,b=b,a
    return a,b

n,m=tuple(map(int,input().split()))
a,b=f(n,m)
print(a,b)