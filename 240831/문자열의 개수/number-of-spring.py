cnt=0
arr=[]
while True:
    msg=input()
    if msg=='0':
        break
    arr.append(msg)
    cnt+=1
print(cnt)
for i in range(len(arr)):
    if i %2==0:
        print(arr[i])