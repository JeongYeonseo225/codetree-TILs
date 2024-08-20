n=int(input())

arr=list(map(int,input().split()))

newarr=[i**2 for i in arr]

for elem in newarr:
    print(elem,end=' ')