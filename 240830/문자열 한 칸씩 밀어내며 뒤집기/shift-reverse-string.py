arr=input().split()
msg=arr[0]
n=int(arr[1])

for _ in range(n):
    num=int(input())
    if num==1:
        msg=msg[1:]+msg[0]
    elif num==2:
        msg=msg[-1]+msg[:-1]
    else:
        msg=msg[::-1]
    print(msg)