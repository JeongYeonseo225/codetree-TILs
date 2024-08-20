arr=list(map(int,input().split()))
newarr=[]

for elem in arr:
    if elem==0:
        break
    newarr.append(elem)

cnt_arr=[0]*10
for elem in newarr:
    elem//=10
    if elem==0:
        continue
    cnt_arr[elem]+=1 

for i in range(1,10):
    print(f"{i} - {cnt_arr[i]}")