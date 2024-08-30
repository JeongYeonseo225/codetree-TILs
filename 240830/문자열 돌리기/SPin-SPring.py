msg =input()

L=len(msg)
print(msg)
for i in range(L):
    
    msg=msg[-1]+msg[:-1]
    print(msg)