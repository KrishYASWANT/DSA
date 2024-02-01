routes=[[0,1],[0,2],[0,3],[1,3],[2,1],[2,3],[3,1],[3,2]]
graph={}
for i in range(5):
    graph[i]=[]

for (u,v) in routes:
    graph[u].append(v)


for item in graph.items():
    print(item)
print(graph)
