msg=input()
msg=list(msg)

msg.pop(1)
msg.pop(-2)

msg=''.join(msg)
print(msg)