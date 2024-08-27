arr=input().split()
s=arr[0]
q=int(arr[1])

for _ in range(q):
    s=list(s)
    arr=input().split()
    num = int(arr[0])
    if num==1:
        a= int(arr[1])
        b= int(arr[2])
        s[a-1],s[b-1]=s[b-1],s[a-1]
    elif num==2:
        a= arr[1]
        b= arr[2]
        for elem in s:
            if a in s:
                s[s.index(a)] = b
    s=''.join(s)
    print(s)