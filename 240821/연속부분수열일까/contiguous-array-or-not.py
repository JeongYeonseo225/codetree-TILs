n1,n2=map(int,input().split())

A=[0]*n1
A=list(map(int,input().split()))

B=[0]*n2
B=list(map(int,input().split()))

#B length 만큼 A를 쪼개기
new_A=[0]*n2
satis=True
for i in range(n1-n2+1):
    for j in range(i,i+6):
        new_A=A[j]
        if new_A==B:
            satis=True

if satis==True:
    print('Yes')
else:
    print('No')