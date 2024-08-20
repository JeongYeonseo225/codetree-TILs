arr=list(map(int,input().split()))
newarr=[]

for elem in arr:
    if elem==0:
        break
    newarr.append(elem)

cnt_arr=[0]*11
for elem in newarr:
    elem//=10
    cnt_arr[elem] +=1

for i in range(10,0,-1):
    print(f"{i}0 - {cnt_arr[i]}")