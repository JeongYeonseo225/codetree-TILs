arr=["apple","banana","grape","blueberry","orange"]

wrd = input()
cnt=0
for elem in arr:
    if wrd == elem[2] or wrd == elem[3]:
        print(elem)
        cnt+=1
print(cnt)