def isvalid(grid,visited,x,y):
    row=len(grid)
    col=len(grid[0])
    if x<0 or y<0 or x>=row or y>=col or visited[x][y]==1 or grid[x][y]=='N':
        return False
    return True
def bfs(grid,visited,start,end):
    queue=[]
    x,y=start[0],start[1]
    visited[x][y]=1
    distance[x][y]=0
    queue.append(start)
    while queue:
        a,b=queue.pop(0)
        #print(grid[a][b])
        for k,l in [[1,0],[0,1],[-1,0],[0,-1]]:
            if isvalid(grid,visited,a+k,b+l):
                visited[a+k][b+l]=1
                queue.append((a+k,b+l))
                distance[a+k][b+l]=distance[a][b]+1
    #for i in distance:
     #   print(i)
    print(distance[end[0]][end[1]])

grid =[['S','N', 'P', 'P', 'P'], 
        ['P', 'P', 'P', 'N', 'P'], 
        ['P','N','N','N', 'P'], 
        ['P','N', 'E', 'P', 'P']]

row = len (grid)
col = len (grid[0])
visited = []
distance = []
for _ in range(row):
    a = []
    b = []
    for _ in range(col):
        a.append(0)
        b.append((-1))
    visited.append(a)
    distance.append(b)

for i in range(row):
    for j in range(col):
        if grid[i][j]=='S':
            start = (i,j)
        if grid[i][j]=='E':
            end = (i,j)
bfs(grid,visited,start,end)