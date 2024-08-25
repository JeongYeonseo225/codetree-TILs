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
    newarr.append(f"{len(elem)}")
 
nRLE=""
for elem in newarr:
    nRLE+=elem

print(len(nRLE))
for elem in nRLE:
    print(elem,end='')