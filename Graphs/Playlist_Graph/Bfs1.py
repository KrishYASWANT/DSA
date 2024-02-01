class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in edges:
            if start not in self.graph_dict:
                self.graph_dict[start]=[end]
            else:
                self.graph_dict[start].append(end)
            if end not in self.graph_dict:
                self.graph_dict[end] = [start]
            else:
                self.graph_dict[end].append(start)
        print(self.graph_dict)
#{1: [2, 6, 7, 8], 2: [3], 3: [6, 4, 5], 7: [9], 9: [0]}

    def bfs(self,visited):
        queue=[]
        queue.append(1)
        visited[1]=True
        while queue:
            temp=queue.pop(0)
            print(temp)
            for child in self.graph_dict[temp]:
                if child not in visited:
                    queue.append(child)
                    visited[child]=True



routes=[[1,2],[1,6],[1,7],[1,8],[2,3],[3,6],[3,4],[3,5],[7,9],[9,8]]
visited={}
route_graph=Graph(routes)
route_graph.bfs(visited)

