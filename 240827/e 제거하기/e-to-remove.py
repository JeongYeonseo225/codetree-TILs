msg=input()
idx=msg.index('e')
msg=list(msg)
msg.pop(idx)
msg=''.join(msg)
print(msg)