n,m=tuple(map(int,input().split()))

num=1
arr=[
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        arr[i][j]=num
        print(num,end=' ')
        num+=1
    print()