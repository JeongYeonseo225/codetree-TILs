y=int(input())

def f_year(n):
    if n%100==0 and n%400!=0:
        return False
    elif n%4==0:
        return True
    return False

if f_year(y)==True:
    print("true")
else:
    print("false")