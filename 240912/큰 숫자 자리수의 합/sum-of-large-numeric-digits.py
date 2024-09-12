a,b,c=list(map(int,input().split()))
num=a*b*c

def f(num):
    if num<10:
        return num
    return f(num//10)+(num%10)

print(f(num))