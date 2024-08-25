arr=[]
for _ in range(10):
    msg=input()
    arr.append(msg)
char=input()

for elem in arr:
    if elem[-1] == char:
        print(elem)