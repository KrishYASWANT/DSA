class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict =  {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print("Graph dict:",self.graph_dict)

    def get_paths(self,start, end,path=[]):
        path=path+[start]

        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths=[]

        for node in self.graph_dict[start]:
            #print(node)
            if node not in path:
                new_paths = self.get_paths(node,end,path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self,start,end):
        return min(self.get_paths(start,end),key=len)
routes=[
    ("Mumbai","Paris"),
    ("Mumbai","Dubai"),
    ("Paris","Dubai"),
    ("Paris","New York"),
    ("Dubai","New York"),
    ("New york","Toronto")
    ]
route_graph=Graph(routes)
start="Paris"
end="New York"
print("Paths from ",start,"To",end,route_graph.get_paths(start,end))
print(f"Shortest path from {start} to {end} is ",route_graph.get_shortest_path(start,end))