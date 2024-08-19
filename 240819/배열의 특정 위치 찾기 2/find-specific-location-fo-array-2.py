arr=list(map(int,input().split()))

print(abs(sum(arr[0::2])-sum(arr[1::2])))