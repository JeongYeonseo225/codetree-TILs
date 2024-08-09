arr = input().split() #input 변수명은 똑같이 써도됨
info1_age = int(arr[0])
info1_gen= arr[1]

arr =input().split()
info2_age=int(arr[0])
info2_gen= arr[1]

if (info1_age>=19 and info1_gen=='M') or (info2_age>=19 and info2_gen=='M'):
    print(1)
else:
    print(0)