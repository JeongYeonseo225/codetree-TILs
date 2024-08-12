a=input().split()
a_sym=a[0]
a_temp=int(a[1])

b=input().split()
b_sym=b[0]
b_temp=int(b[1])

c=input().split()
c_sym=c[0]
c_temp=int(c[1])

if a_sym=='Y' and a_temp>=37:
    a_emg = 'A'
elif a_sym=='N' and a_temp>=37:
    a_emg ='B'
elif a_sym=='Y' and a_temp<37:
    a_emg='C'
else:
    a_emg='D'

if b_sym=='Y' and b_temp>=37:
    b_emg = 'A'
elif b_sym=='N' and b_temp>=37:
    b_emg ='B'
elif b_sym=='Y' and b_temp<37:
    b_emg='C'
else:
    b_emg='D'

if c_sym=='Y' and c_temp>=37:
    c_emg = 'A'
elif c_sym=='N' and c_temp>=37:
    c_emg ='B'
elif c_sym=='Y' and c_temp<37:
    c_emg='C'
else:
    c_emg='D'

if (a_emg=='A' and b_emg=='A') or (b_emg=='A' and c_emg=='A') or (a_emg=='A' and c_emg=='A'):
    print('E')
else:
    print('N')