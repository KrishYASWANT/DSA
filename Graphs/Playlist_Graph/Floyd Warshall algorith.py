ipt = [[1,3,2], [1,2,-1], [2,3,3], [3,5,2], [2,5,1], [3,4,1], [4,5,2]]
n = 5
row = n+1
col = n+1
graph = []
for i in range (row):
	temp = []
	for j in range(col):
		temp.append(10**8+1)
	graph.append(temp)
for i in range (row):
	for j in range(col):
		if i==j:
			graph[i][j] = 0
for u, v,d in ipt:
	graph [u] [v] = d

for k in range(1,n+1):
	for i in range(1, row):
		for j in range(1,col):
			if i==j or i==k or j==k:
				pass
			else:
				if graph[i][k]+graph [k] [j] <graph[i][j]:
					graph[i][j]=graph[i][k]+graph [k][j]

for i in graph:
	print(i)