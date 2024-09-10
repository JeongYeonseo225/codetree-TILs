def f(n):
    sum_val=0
    for i in range(1,n+1):
        sum_val+=i
    sum_val//=10
    print(sum_val)

num=int(input())
f(num)