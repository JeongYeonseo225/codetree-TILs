hos_arr=[0]*4

for _ in range(3):
    arr=input().split()
    sym=arr[0]
    tmp=int(arr[1])
    if sym=='Y' and tmp>=37:
        hos_arr[0]+=1
    elif sym=='N' and tmp>=37:
        hos_arr[1]+=1
    elif sym=='Y' and tmp<37:
        hos_arr[2]+=1
    else:
        hos_arr[3]+=1

for elem in hos_arr:
    print(elem,end=' ')

if hos_arr[0]>=2:
    print('E')