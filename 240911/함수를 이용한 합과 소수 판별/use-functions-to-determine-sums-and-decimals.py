def f(a):
    for i in range(2,a):
        if a%i==0:
            return False
    a1=str(a)
    sum_val=0
    for elem in a1:
        sum_val+=int(elem)
    if sum_val%2==0:
        return True
    return False


a,b=tuple(map(int,input().split()))
cnt=0
for i in range(a,b+1):
    if f(i)==True:
        cnt+=1

print(cnt)