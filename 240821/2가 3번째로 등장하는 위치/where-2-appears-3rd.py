n=int(input())
arr=list(map(int,input().split()))

cnt=0
for idx, elem in enumerate(arr):
    if elem == 2:
        cnt+=1
    if cnt==3:
        print(idx+1)
        break