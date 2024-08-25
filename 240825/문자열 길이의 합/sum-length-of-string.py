n=int(input())

length,cnt=0,0
for _ in range(n):
    msg=input()
    length+=len(msg)
    if 'a' == msg[0]:
        cnt+=1
print(length,cnt)