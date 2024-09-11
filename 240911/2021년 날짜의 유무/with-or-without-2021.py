def calendar(M,D):
    if M==2:
        if D>0 and D<29:
            return True
    elif M==4 or M==6 or M==9 or M==11:
        if D>0 and D<31:
            return True
    elif 1<=M<=12:
        if 0<D<32:
            return True
        

M,D=tuple(map(int,input().split()))

if calendar(M,D)==True:
    print("Yes")
else:
    print("No")