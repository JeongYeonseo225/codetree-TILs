clss=0
corr=0
toil=0
n=int(input())

i=1
while i<=n:
    if i%12==0:
        toil+=1
    elif i%3==0:
        corr+=1
    elif i%2==0:
        clss+=1
    i+=1
print(clss,corr,toil)