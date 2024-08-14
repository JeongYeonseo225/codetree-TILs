cnt=0
while True:
    n=int(input())
    if n%2==1:
        continue
    else:
        quo=n//2
        print(quo)
        cnt+=1
        if cnt==3:
            break