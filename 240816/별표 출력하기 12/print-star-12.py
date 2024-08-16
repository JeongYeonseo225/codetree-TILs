n=int(input())
#n이 1일땐 1x1
#n이 짝수일 땐 nxn
#n이 홀수일 땐 (n-1)xn

if n==1 or n%2==0:
    for i in range(1,n+1):
        for j in range(1, n+1):
            if i==1 or j==n or (j%2==0 and i<=j):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
else: 
    for i in range(1, n):
        for j in range(1,n+1):
            if i==1 or (j%2==0 and i<=j):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()