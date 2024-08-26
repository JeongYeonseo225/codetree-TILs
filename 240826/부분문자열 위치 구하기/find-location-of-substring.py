msg = input()
part = input()

if part in msg:
    print(msg.index(part))
else:
    print(-1)