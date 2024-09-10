a,b=tuple(map(int,input().split()))
# tuple은 소괄호로 묶인거고, list는 대괄호로 묶인거네..

def f(n):
    n = str(n)
    if '3' in n:
        return True
    elif '6' in n:
        return True
    elif '9' in n:
        return True
    return False

def g(n):
    if n%3==0:
        return True

cnt=0
for i in range(a,b+1):
    if f(i)==True:
        cnt+=1
    elif g(i)==True:
        cnt+=1

print(cnt)