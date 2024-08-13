arr=input().split()
a=int(arr[0])
b=int(arr[1])

# 정수부분 소수부분 나눠서 처리하면?
quo = a//b
rem = a%b
print(f"{quo}.",end='') #정수

for _ in range(20): #소수 21번째에서 버림이므로 20번째자리까지 나타내줘야함.
    rem*=10
    quo = rem//b
    rem=rem%b
    print(quo,end='')