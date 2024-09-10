def f(a,b,c):
    arr=[]
    arr.append(a)
    arr.append(b)
    arr.append(c)
    return min(arr)

num1,num2,num3=list(map(int,input().split()))
print(f(num1,num2,num3))