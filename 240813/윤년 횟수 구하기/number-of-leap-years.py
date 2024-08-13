n=int(input())
cnt=0

i=1
while i<=n:
    if i%400==0:
        cnt+=1
    elif i%100==0 and i%400!=0:
        cnt=cnt
    elif i%4==0:
        cnt+=1
    i+=1 #while문은 항상 항~~~상 +=1조건 충족시켜야함!!
print(cnt)