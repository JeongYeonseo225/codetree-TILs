msg=input()
ee_cnt,eb_cnt=0,0
for i in range(len(msg)-1):
    if msg[i]=='e' and msg[i+1]=='e':
        ee_cnt+=1
for i in range(len(msg)-1):
    if msg[i]=='e' and msg[i+1]=='b':
        eb_cnt+=1
print(ee_cnt,eb_cnt)