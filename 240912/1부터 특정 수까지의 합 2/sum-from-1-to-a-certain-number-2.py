N=int(input())

def f(N):
    if N==1:
        return 1
    return f(N-1)+N

print(f(N))