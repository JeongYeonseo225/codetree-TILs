a=int(input())

if a%2==0:
    a//=2

if a%2==1:
    a+=1
    a//=2

print(a) # 그냥 나누기는 실수값이 결과가 되므로 //로 몫으로 설정해주어야 함
#만약에 홀수가 처음에 받아졌을 때 안에다가 식을 넣으면 그 값이 그냥 나오기 때문에 관계없이 순서만 지켜서 넣는게 맞는듯