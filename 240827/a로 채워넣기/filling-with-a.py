msg=input()
msg=list(msg)

msg[1]='a'
msg[-2]='a'

msg=''.join(msg)
print(msg)