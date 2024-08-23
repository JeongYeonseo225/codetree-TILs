n1,n2=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
newarr=[]

satisfied=False
for i in range(n2-n1+1):
    newarr=A[i:i+n2]
    for i in range(len(newarr)):
        if newarr[i]==B[i]:
            satisfied=True

if satisfied==True:
    print('Yes')
else:
    print('No')