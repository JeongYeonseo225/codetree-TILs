n=int(input())
arr=list(map(int,input().split()))
newarr=[]

for idx,elem in enumerate(arr):
    newarr.append(elem)
    if idx%2==0:
        newarr.sort()
        length=len(newarr)
        print(newarr[length//2],end=' ')