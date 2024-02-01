def gcd(m,n):
	a=1
	for i in range(1,min(m,n)+1):
		if(m%i==0 and n%i==0):
			a=i
	print(a)

gcd(456,36)
gcd(1089,45)