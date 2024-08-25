arr=[]
for _ in range(10):
    msg=input()
    arr.append(msg)
char=input()

satis=False
for elem in arr:
    if elem[-1] == char:
        print(elem)
        satis=True

if satis==False:
    print('None')