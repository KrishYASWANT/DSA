import heapq
class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end, weight):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append((end, weight))

    # the problem with this algorithm is it doesn't work with negetive loads/time/distance/cost
    def dijkstra(self, start, end):
        priority_queue = [(0, start)]
        visited = set()

        while priority_queue:
            current_weight, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == end:
                return current_weight

            for neighbor, edge_weight in self.graph.get(current_node, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (current_weight + edge_weight, neighbor))

        return float('inf')

# Example usage
graph = WeightedGraph()

# Add edges to the graph
edges = [[2, 9, 2], [7, 2, 3], [7, 9, 7], [9, 5, 1]]
for edge in edges:
    graph.add_edge(edge[0], edge[1], edge[2])

# Find the shortest time from 7 to 9
shortest_time = graph.dijkstra(7, 9)

print(f"Shortest time from 7 to 9: {shortest_time}")
