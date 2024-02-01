class Grid:
    def dfs(self,grid,visited,start):
        i,j=start[0],start[1]
        queue=[]
        visited[i][j]=1
        queue.append(start)
        while queue:
            x,y=queue.pop(0)
            print(grid[x][y])
            for k,l in [[1,0],[0,1],[-1,0],[0,-1]]:
                if self.isvalid(grid,visited,x+k,y+l):
                    visited[x+k][y+l]=1
                    queue.append((x+k,y+l))
                    
    def isvalid(self,grid,visited,x,y):
        row,col=len(grid),len(grid[0])
        if x<0 or y<0 or x>=row or y>=col or visited[x][y]==1:
            return False
        return True
        
grid = [[3,1,5], [7,8,2], [14,11,9]]
visited = [[0] * len(grid[0]) for _ in range(len(grid))]  # Correct initialization
g = Grid()
g.dfs(grid, visited, (0, 0))
