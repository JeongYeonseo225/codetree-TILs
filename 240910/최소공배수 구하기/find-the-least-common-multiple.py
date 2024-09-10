def f(a,b):
    arr=[]
    for i in range(a,a*b+1):
        if i%a==0 and i%b==0:
            arr.append(i)
    print(min(arr))

num1,num2=tuple(map(int,input().split()))
f(num1,num2)