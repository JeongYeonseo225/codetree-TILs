msg=input()

while True:
    arr=list(msg)
    idx=int(input())
    if idx>len(arr)-1:
        arr.pop(-1)
    else:
        arr.pop(idx)
    msg=''.join(arr)
    print(msg)
    if len(msg) ==1:
        break