def f(a):
    for i in range(1,len(a)):
        if a[0] != a[i]:
            return True

A=input()

if f(A)==True:
    print("Yes")
else:
    print("No")