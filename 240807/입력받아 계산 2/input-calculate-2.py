arr=input().split() #list형은 int로 바꿔서 처리 안되기 때문에, 맨 위에서 int로 감싸기 불가능, map(int, arr) 이런식으로 넣어야될 듯?
a=int(arr[0])
b=int(arr[1])
print(a*b)