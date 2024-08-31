n1,n2=tuple(map(int,input().split()))

A=list(map(int,input().split()))
B=list(map(int,input().split()))

satis=False

for i in range(n1-n2+1):
    newarr=[]
    for j in range(i,i+n2):
        newarr.append(A[j])
    if newarr==B:
        satis=True

if satis==True:
    print('Yes')
else:
    print('No')