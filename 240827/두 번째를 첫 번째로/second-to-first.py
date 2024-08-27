msg=input()

msg=list(msg)
a=msg[1]
for elem in msg:
    if elem ==a:
        elem=msg[0]
    print(elem,end='')