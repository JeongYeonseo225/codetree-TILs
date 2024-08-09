a=input().split()
am=int(a[0])
ae=int(a[1])

b=input().split()
bm=int(b[0])
be=int(b[1])

if am>bm:
    print('A')
elif am<bm:
    print('B')
else:
    if ae>be:
        print('A')
    elif ae<be:
        print('B')