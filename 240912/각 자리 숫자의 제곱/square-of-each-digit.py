N=int(input())


def f(N):
    if N<10:
        return N**2
    return (N%10)**2+f(N//10)

print(f(N))