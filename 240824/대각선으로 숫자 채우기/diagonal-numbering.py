n,m=tuple(map(int,input().split()))

arr=[
    [0 for _ in range(m)]
    for _ in range(n)
]

num=1
for cnt in range(0,n+m-1):
    for i in range(n):
        for j in range(m):
            if i+j==cnt:
                arr[i][j]=num
                num+=1
            

for row in arr:
    for elem in row:
        print(elem,end=' ')
    print()