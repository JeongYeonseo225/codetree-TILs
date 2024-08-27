msg=input()
msg=list(msg)

for elem in msg:
    if elem ==msg[0]:
        elem = msg[1]
    elif elem == msg[1]:
        elem = msg[0]
    print(elem, end='')