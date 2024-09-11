def f(a,b):
    a,b=b,a
    return a,b

n,m=tuple(map(int,input().split()))
for elem in f(n,m):
    print(elem,end=' ')