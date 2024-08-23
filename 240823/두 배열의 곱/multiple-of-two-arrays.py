arr1=[
    list(map(int,input().split()))
    for _ in range(3)
]
e = input() # 엔터
arr2=[
    list(map(int,input().split()))
    for _ in range(3)
]

newarr=[
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        newarr[i][j] = arr1[i][j] * arr2[i][j]
        print(newarr[i][j],end=' ')
    print()