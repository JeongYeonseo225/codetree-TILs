def f_abs(arr):
    newarr=[]
    for elem in arr:
        newarr.append(abs(elem))
    return newarr 

N=int(input())
arr=list(map(int,input().split()))
for elem in f_abs(arr):
    print(elem,end=' ')