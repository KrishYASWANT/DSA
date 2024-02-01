# the issue with this algorithm is is we have a negitive cycle this algorithm fails.

ipt=[[1,2,2],[1,3,1],[2,3,-2],[2,4,2],[3,5,-1],[4,5,1]]
n=5
distance={}
for i in range(1,n+1):
	distance[i]=float('inf')

distance[1]=0
for _ in range(n-1):
	for u,v,d in ipt:
		if distance[u]<float('inf') and d+distance[u]<distance[v]:
			distance[v]=distance[u]+d

print(distance)