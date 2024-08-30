A=input()
msg=input()
msgarr=list(msg)

for elem in msgarr:
    if 'L' ==elem:
        A=A[1:]+A[0]
    elif 'R' ==elem:
        A=A[-1]+A[:-1]
print(A)