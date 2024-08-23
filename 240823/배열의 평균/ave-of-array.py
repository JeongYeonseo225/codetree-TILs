arr=[
    list(map(int,input().split()))
    for _ in range(2)
]


for i in range(2):
    hor_sum=0
    for j in range(4):
        hor_sum+=arr[i][j]
    print(f"{hor_sum/4:.1f}",end=' ')
print()

for j in range(4):
    ver_sum=0
    for i in range(2):
        ver_sum+=arr[i][j]
    print(f"{ver_sum/2:.1f}",end=' ')
print()

sum_val=0
for i in range(2):
    for j in range(4):
        sum_val+=arr[i][j]
print(f"{sum_val/8:.1f}")