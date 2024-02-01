# def fib(n):
# 	a,b=0,1
# 	c=0
# 	while c<n:
# 		a,b=b,a+b
# 		c+=1
# 	return a

def fib(n):
	a,b=0,1
	for i in range(n):
		a,b=b,a+b
	return a

	 
print(fib(25))

