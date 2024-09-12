N=int(input())

def f(N):
    if N==0:
        return
    f(N-1)
    print("*"*N)

f(N)