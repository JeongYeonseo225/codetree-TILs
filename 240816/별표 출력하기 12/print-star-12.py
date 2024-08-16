n=int(input())
if n==1:
    print('*')
elif n%2==0: #짝수
    for i in range(1,n+1):
        for j in range(1, n+1):
            if i==1 or (j%2==0 and j==n):
                print('*',end=' ')
            else:
                print(' ',end=' ')
else: #홀수
    for i in range(1, n):
        for j in range(1,n+1):
            if i==1 and j==n:
                print('*',end=' ')
            else:
                print(' ',end=' ')