n,m=tuple(map(int,input().split()))
An=list(map(int,input().split()))

def f(m):
    for _ in range(m):
        sum_val=0
        a1,a2=tuple(map(int,input().split()))
        for i in range(a1-1,a2):
            sum_val+=An[i]
        print(sum_val)

f(m)