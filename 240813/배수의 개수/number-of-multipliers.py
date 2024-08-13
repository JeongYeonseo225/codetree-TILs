th_cnt=0
fv_cnt=0
for _ in range(10):
    n=int(input())
    if n%3==0:
        th_cnt+=1
    if n%5==0:
        fv_cnt+=1
print(th_cnt,fv_cnt)