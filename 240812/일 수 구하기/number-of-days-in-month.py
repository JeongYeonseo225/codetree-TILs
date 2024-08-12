n=int(input())
if (n<=7 and n%2==1) or (n>7 and n%2==0):
    print(31)
elif (n>7 and n%2==1) or (n==4) or n==6:
    print(30)
else:
    print(28)