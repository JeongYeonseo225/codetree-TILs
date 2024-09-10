num=int(input())
def f(n):
    a=n//10
    b=n%10
    return n%2==0 and (a+b)%5==0
    
if f(num) ==True:
    print("Yes")
else:
    print("No")