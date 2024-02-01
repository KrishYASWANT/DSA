def isvalid(grid,visited,x,y):
    row=len(grid)
    col=len(grid[0])
    if x<0 or y<0 or x>=row or y>=col or visited[x][y]==1:
        return False
    return True
def dfs(grid, visited, start):
    i, j =start[0], start [1]
    print (grid[i][j])
    visited[i][j] = 1
    if isvalid (grid, visited,i,j+1): 
        dfs (grid, visited, (i, j+1))
    if isvalid (grid, visited, i,j-1): 
        dfs (grid, visited, (i,j-1))
    if isvalid (grid, visited, i+1,j):
        dfs (grid, visited, (i+1,j))
    if isvalid (grid, visited, i-1,j):
        dfs (grid, visited, (i-1,j))
        
grid = [[3,1,5], [7,8,2], [14,11,9]]
row = len(grid)
col = len (grid[0])
visited = []

for _ in range(row):
    temp = []
    for _ in range(col):
        temp.append(0) 
    visited.append(temp)
dfs(grid,visited,(0,0))