Y,M,D=list(map(int,input().split()))

season=""
if 3<=M<=5:
    season="Spring"
elif 6<=M<=8:
    season="Summer"
elif 9<=M<=11:
    season="Fall"
else:
    season="Winter"

yunyear=0
if Y%400==0:
    yunyear=1
elif Y%100==0:
    yunyear=0
elif Y%4==0:
    yunyear=1
else:
    yunyear=0

tf=False
if yunyear==1:
    if M==2 and 1<=D<=29:
        tf =True
    elif (M==6 or M==9 or M==11 or M==4) and 1<=D<=30:
        tf=True
    elif (M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12) and 1<=D<=31:
        tf =True
else:
    if M==2 and 1<=D<=28:
        tf =True
    elif (M==6 or M==9 or M==11 or M==4) and 1<=D<=30:
        tf=True
    elif (M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12) and 1<=D<=31:
        tf =True

if tf==True:
    print(season)
else:
    print(-1)