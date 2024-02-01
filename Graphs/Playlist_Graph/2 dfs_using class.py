class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in edges:
            if start not in self.graph_dict:
                self.graph_dict[start]=[end]
            else:
                self.graph_dict[start].append(end)

        print(self.graph_dict)
        #
    def dfs(self,node,visited=None):
        if visited is None:
            visited=set()
        print(node)
        visited.add(node)
        for child in self.graph_dict.get(node,[]):
            if child not in visited:
                self.dfs(child,visited)
    def get_path(self,start,end,path=[]):
        path=path + [start]
        if start==end:
            return [path]
        if start not in self.graph_dict:
            return 
        paths=[]
        for child in self.graph_dict[start]:
            if child not in path:
                new_path=self.get_path(child,end,path)
                for p in new_path:
                    paths.append(p)
                
        return paths
    def get_shortest_path(self,start,end,path=[]):
        path=path+[start]
        shortest_path=None
        if start==end:
            return path
        if start not in self.graph_dict:
            return None
        for child in self.graph_dict[start]:
            if child not in path:
                sp=self.get_shortest_path(child,end,path)
                if sp:
                    if shortest_path==None or len(sp)<len(shortest_path):
                        shortest_path = sp
        return shortest_path
    
    def get_shortest_path_(self,start,end):
        return min(self.get_path(start,end),key=len)

    def cyclic_detection(self,node,visited,par):
        visited[node]=1
        for child in self.graph_dict[node]:
            if child not in visited:
                return self.cyclic_detection(child,visited,node)
            else:
                if child!=par:
                    return True
        return False
        
routes=[[0,1],[0,2],[0,3],[1,3],[2,1],[2,3],[3,1],[3,2]]
route_graph=Graph(routes)
route_graph.dfs(0)
start=0
end=3
visited={}
print(route_graph.get_path(start,end))
print(route_graph.get_shortest_path(start,end))
print(route_graph.get_shortest_path_(start,end))
print(route_graph.cyclic_detection(1, visited,-1))
