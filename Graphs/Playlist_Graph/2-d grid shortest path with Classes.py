class Grid:
    def __init__(self):
        self.all_paths = []

    def dfs(self, grid, visited, start, end, path):
        i, j = start[0], start[1]
        path.append(grid[i][j])
        visited[i][j] = 1

        if start == end:
            self.all_paths.append(path.copy())

        for a, b in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + a, j + b
            if self.isvalid(grid, ni, nj, visited):
                self.dfs(grid, visited, (ni, nj), end, path)

        path.pop()
        visited[i][j] = 0  # Backtrack

    def isvalid(self, grid, x, y, visited):
        r, c = len(grid), len(grid[0])
        if x < 0 or y < 0 or x >= r or y >= c or visited[x][y] == 1:
            return False
        return True

    def get_all_paths(self, grid, start, end):
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        self.all_paths = []  # Reset paths before a new call
        self.dfs(grid, visited, start, end, [])
        return self.all_paths
        
    def shortest_path(self,grid,start,end):
        a=self.get_all_paths(grid,start,end)
        short=sum(a[0])
        big=sum(a[0])
        for i in a:
            if short>sum(i):
                short=sum(i)
            if big<sum(i):
                big=sum(i)
        print("shortest path is", short)
        print("longest path is ",big)
            


# Example usage:
grid = [[3, 1, 5], [7, 8, 2], [14, 11, 9]]
g = Grid()
start_index = (0, 0)
end_index = (2, 2)
paths = g.get_all_paths(grid, start_index, end_index)
print(paths)
g.shortest_path(grid, start_index, end_index)
