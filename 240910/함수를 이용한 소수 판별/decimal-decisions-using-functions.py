a,b=tuple(map(int,input().split()))

def prime_num(n):
    if n==1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return False #return은 만나면 즉시 종료 False=0, True=1임 
    return n

def prime_sum(a,b):
    sum_val=0
    for i in range(a,b+1):
        sum_val+=prime_num(i)
    return sum_val

print(prime_sum(a,b))