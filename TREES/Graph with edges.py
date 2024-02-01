class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u in self.adj_list:
            self.adj_list[u].append(v)
        else:
            self.adj_list[u] = [v]

    def remove_edge(self, u, v):
        if u in self.adj_list and v in self.adj_list[u]:
            self.adj_list[u].remove(v)

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_visit(start_vertex, visited)

    def _dfs_visit(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end="->")

        if vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    self._dfs_visit(neighbor, visited)


graph = Graph()


graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(4, 7)
graph.add_edge(5, 8)
graph.add_edge(6, 9)

print("DFS Starting from vertex 1:")
graph.dfs(1)
 
