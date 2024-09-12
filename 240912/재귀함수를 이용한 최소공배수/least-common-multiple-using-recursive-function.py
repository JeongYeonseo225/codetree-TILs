n=int(input())
arr=list(map(int,input().split()))

def g(a,b):
    for i in range(a,a*b+1):
        if i%a==0 and i%b==0:
            return i

def f(n):
    if n==1:
        return arr[n-1]
    return g(f(n-1),arr[n-1])

print(f(n))