msg=input()
arr=[]
for idx,elem in enumerate(msg):
    if idx%2==1:
        arr.append(elem)

for elem in arr[::-1]:
    print(elem,end='')