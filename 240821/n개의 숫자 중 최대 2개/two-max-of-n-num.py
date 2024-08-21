n=int(input())

arr=list(map(int,input().split()))
for _ in range(n):
    for i in range(n-1): #0~8
        if arr[i]<arr[i+1]: #0<1...8<9
            arr[i],arr[i+1]=arr[i+1],arr[i]

print(arr[0],arr[1])