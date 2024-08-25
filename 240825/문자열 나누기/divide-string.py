n=int(input())
arr=input().split()

arr=''.join(arr) # 문자열 리스트일때만 조인가능
for idx,elem in enumerate(arr):
    print(elem,end='')
    if (idx+1)%5==0:
        print()