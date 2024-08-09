a=input().split()
a_m=int(a[0])
a_e=int(a[1])

b=input().split()
b_m=int(b[0])
b_e=int(b[1])

if a_m>b_m and a_e>b_e:
    print(1)
else:
    print(0)