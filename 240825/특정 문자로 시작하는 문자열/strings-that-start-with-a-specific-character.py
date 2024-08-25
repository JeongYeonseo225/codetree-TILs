n=int(input())
arr=[]

for _ in range(n):
    arr.append(input())

wrd=input()
cnt,avg=0,0
for elem in arr:
    if wrd==elem[0]:
        cnt+=1
        avg+=len(elem)
print(cnt,f"{avg/cnt:.2f}")