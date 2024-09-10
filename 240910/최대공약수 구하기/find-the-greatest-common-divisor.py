def print_max_div(n,m):
    arr=[]
    for i in range(1,n+1):
        if n%i==0 and m%i==0:
            arr.append(i)
    print(max(arr))

num1,num2=tuple(map(int,input().split()))
print_max_div(num1,num2)