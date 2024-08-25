A=input()
RLE=""

wrd=A[0]
cnt=0
for elem in A:
    if wrd==elem:
        RLE+=wrd
    else:
        RLE+=' '
        wrd=elem
        RLE+=wrd   

arr=RLE.split()
newarr=[]
for elem in arr:
    newarr.append(elem[0])
    newarr.append(len(elem))
print(len(newarr))
for elem in newarr:
    print(elem,end='')