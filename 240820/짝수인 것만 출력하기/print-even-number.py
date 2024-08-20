n=int(input())
arr=list(map(int,input().split()))

newarr = [elem for elem in arr if elem%2==0]
for elem in newarr:
    print(elem,end=' ')