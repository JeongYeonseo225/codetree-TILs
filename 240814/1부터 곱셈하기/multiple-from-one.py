n=int(input())

mulval=1
for i in range(1,11):
    mulval*=i
    if mulval>=n:
        print(i)
        break