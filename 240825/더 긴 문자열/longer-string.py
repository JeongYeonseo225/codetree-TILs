wrd1,wrd2=input().split()

if len(wrd1)>len(wrd2):
    print(wrd1,len(wrd1))
elif len(wrd1)<len(wrd2):
    print(wrd2,len(wrd2))
else:
    print('same')