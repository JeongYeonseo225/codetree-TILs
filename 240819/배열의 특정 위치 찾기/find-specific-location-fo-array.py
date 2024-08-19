arr=list(map(int,input().split()))

sumval=0
for elem in arr[1::2]:
    sumval+=elem
print(sumval,end=' ')


newarr = arr[2::3]
print(f"{sum(newarr)/len(newarr):.1f}")