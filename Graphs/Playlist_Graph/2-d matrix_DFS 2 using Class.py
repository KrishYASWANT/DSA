class Grid:
    def dfs(self,grid,visited,start):
        i,j=start[0],start[1]
        print(grid[i][j])
        visited[i][j]=1
        for a,b in [[1,0],[0,1],[-1,0],[0,-1]]:
            if self.isvalid(grid,i+a,j+b,visited):
                self.dfs(grid,visited,(i+a,j+b))      
    '''        IMPORTANT     
    Using the above method we can create a sprial matrix from the original matrix    
    '''
    def isvalid(self,grid,x,y,visited):
        r,c = len(grid),len(grid[0])
        if x<0 or y<0 or x>=r or y>=c or visited[x][y]==1:
            return False
        return True

grid = [[3,1,5], [7,8,2], [14,11,9]]
visited=[ [0]*len(grid[0]) for i in range(len(grid))]
print(visited)
g=Grid()
g.dfs(grid,visited,(0,0))