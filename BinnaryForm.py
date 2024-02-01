
def binnary(n):
	assert int(n)==n ,'The number should be int'
	if n==0:
		return 0
	else:
		#print('n%2;',n%2,'    ',10*binnary(int(n/2)))
		return n%2+10*binnary(int(n/2))

print(binnary(10))