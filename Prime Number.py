'''Prime Number Code'''

def prime(n):
	a=[]
	for i in range(2,n):
		c=0
		for j in range(2,i):
			if i%j==0:
				c+=1
		if c==0:
			a.append(i)
	print(a)

	
>>> prime(24)
[2, 3, 5, 7, 11, 13, 17, 19, 23]