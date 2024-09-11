def f(arr):
    for elem in arr:
        if elem%2==0:
            elem//=2
        print(elem, end=' ')
        
N=int(input())
arr=list(map(int,input().split()))

f(arr)