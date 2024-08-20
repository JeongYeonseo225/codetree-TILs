n=int(input())
arr=list(map(int,input().split()))

cnt_arr=[0]*9
for elem in arr:
    cnt_arr[elem-1] +=1

for elem in cnt_arr:
    print(elem)