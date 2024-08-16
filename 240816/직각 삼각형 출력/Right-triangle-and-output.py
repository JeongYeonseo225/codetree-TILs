n=int(input())

for i in range(1,n+1):
    for j in range(1,2*i): #마지막은 값이 포함안된다는 것도 기억 !
        print('*',end='')
    print()