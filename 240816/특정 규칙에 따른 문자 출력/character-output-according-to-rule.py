n=int(input())

for i in range(1, 2*n):
	if i<=n:
		for blank in range(n-i):
			print(' ',end=' ')
		for j in range(i):
			print('@',end=' ')
	else:
		for j in range(2*n-i):
			print('@',end=' ')
		for blank in range(i-n):
			print(' ',end=' ')
	print()