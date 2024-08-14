while True:
    arr=input().split()
    wid = int(arr[0])
    leng =int(arr[1])
    char = arr[2]
    print(wid*leng)
    if char=='C':
        break