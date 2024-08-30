msg=input()
for elem in msg:
    if elem>'Z':
        print(elem.upper(),end='')
    else:
        print(elem.lower(),end='')