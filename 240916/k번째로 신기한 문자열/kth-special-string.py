n,k,T=input().split()
n=int(n)
k=int(k)
arr=[]

for _ in range(n):
    word=input()
    if T in word[0:len(T)]:
        arr.append(word)
arr.sort()
print(arr[k-1])