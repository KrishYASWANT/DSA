def dfs(graph,node,visited=set()):
    print(node)
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            dfs(graph,child,visited)


routes=[[1,2],[1,5],[2,3],[2,4],[2,5],[3,4],[3,6],[4,5],[4,6],[5,6]]
graph={}
n=6
for i in range(1,n+1):
    graph[i]=[]

for (u,v) in routes:
    graph[u].append(v)
    graph[v].append(u)     # comment this line if it is uni-directional graph

print("The present Graph is ",graph)
#{1: [2, 5], 2: [1, 3, 4, 5], 3: [2, 4, 6], 4: [2, 3, 5, 6], 5: [1, 2, 4, 6], 6: [3, 4, 5]}
dfs(graph,2) # it is visiting every node from the present node.
