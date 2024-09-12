def f(a,b):
    arr=[]
    arr.append(a)
    arr.append(b)
    return min(arr)*2, max(arr)+25

a,b=tuple(map(int,input().split()))
mi,ma=f(a,b)
print(mi,ma)