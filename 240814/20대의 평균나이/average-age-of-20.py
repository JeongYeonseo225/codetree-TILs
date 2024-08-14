age,cnt=0,0
while True:
    n=int(input())
    if n<20 or n>29:
        break
    age+=n
    cnt+=1
print(f"{age/cnt:.2f}")