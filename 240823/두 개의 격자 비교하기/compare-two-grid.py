n,m=tuple(map(int,input().split()))
arr1=[
    list(map(int,input().split()))
    for _ in range(n)
]
arr2=[
    list(map(int,input().split()))
    for _ in range(n)
]

newarr=[
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        if arr1[i][j] ==arr2[i][j]:
            newarr[i][j] =0
        else:
            newarr[i][j]=1
        print(newarr[i][j],end=' ')
    print()