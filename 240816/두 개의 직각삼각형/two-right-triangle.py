n=int(input())

for i in range(n): #i==1
    for j in range(n-i):
        print('*',end='')
    for blank in range(2*i):
        print(' ',end='')   
    for j in range(n-i):
        print('*',end='')
    print()