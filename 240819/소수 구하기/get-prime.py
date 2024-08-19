n=int(input())
#소수는 1과 자기자신만 약수로 가짐

for i in range(1, n+1):
    if i==1:
        continue
    isPrime=True
    for j in range(2,i):
        if i%j==0:
            isPrime=False
    if isPrime==True:
        print(i,end=' ')