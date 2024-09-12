N=int(input())
cnt=0

def f(N):
    global cnt
    if N==1:
        return
    
    if N%2==0:
        f(N//2)
        cnt+=1
    else:
        f(N//3)
        cnt+=1
    return cnt

print(f(N))