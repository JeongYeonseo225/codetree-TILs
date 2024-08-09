info1 = input().split()
info1_age = int(info1[0])
info1_gen= info1[1]

info2 =input().split()
info2_age=int(info2[0])
info2_gen= info2[1]

if (info1_age>=19 and info1_gen=='M') or (info2_age>=19 and info2_gen=='M'):
    print(1)
else:
    print(0)