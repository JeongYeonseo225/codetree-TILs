n=int(input())
arr=[
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    num=i+1
    for j in range(n):
        arr[i][j]=num
        num+=n
        print(arr[i][j],end=' ')
    print()