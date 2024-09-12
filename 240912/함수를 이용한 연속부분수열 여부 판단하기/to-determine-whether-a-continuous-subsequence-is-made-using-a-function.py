def cont_part_seq(A,B,n1,n2):
    for i in range(n1-n2+1):
        part_A=[]
        for j in range(i,i+n2):
            part_A.append(A[j])
        if part_A!=B:
            continue
        else:
            return True

n1,n2=tuple(map(int,input().split()))

A=list(map(int,input().split()))
B=list(map(int,input().split()))


if cont_part_seq(A,B,n1,n2)==True:
    print("Yes")
else:
    print("No")