# def gcd(m,n):
# 	a=1
# 	for i in range(min(m,n),1,-1):
# 		if(m%i==0 and n%i==0):
# 			a=i
# 			break
# 	print(a)

#Eulid's Algorithm
#First way
def gcd(m,n):
	if m<n: # Assume m>=n
		(m,n)=(n,m)
	while(m%n)!=0:
		diff=m-n
		(m,n)=(max(n,diff),min(n,diff))
		print(max(n,diff),'  ',min(n,diff),m,"  ",n)
	return(n)

#Secound way

# def gcd(a,b):
# 	assert int(a)==a and int(b)==b, 'The number should be int'
# 	if a<0:
# 		a= a*-1
# 	if b<0:
# 		b=b*-1
# 	if b==0:
# 		return a
# 	else:
# 		return gcd(b,a%b)


print(gcd(456,36))
print(gcd(1089,45))
print(gcd(48,18))