n=int(input())

for i in range(n):
    for j in range(n-i):
        for l in range(n-i):
            print('*',end='')
        print(' ',end='')
    print()