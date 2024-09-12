N=int(input())

def HelloWorld(n):
    if n==0:
        return
    HelloWorld(n-1)
    print("HelloWorld")

HelloWorld(N)