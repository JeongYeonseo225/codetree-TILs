n=int(input())
sat=False
for i in range(1,n):
    if n%i==0 and i==1:
        sat=True
if sat==True:
    print('P')
else:
    print('C')