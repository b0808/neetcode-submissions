from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        m = len(grid)
        n = len(grid[0])
        visted = [[0 for j in range(n)] for i in range(m)]
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        que  = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    que.append((i,j,0))

        while len(que)!= 0:
            i,j,dis = que.popleft()
            grid[i][j]  = min(dis,grid[i][j])
            visted[i][j] = 1
            for x,y in d:
                new_i,new_j = i+x,j+y
                if new_i<0 or new_i>=m or new_j<0 or new_j>=n or visted[new_i][new_j] ==1:
                    continue
                if grid[new_i][new_j] == -1 or grid[new_i][new_j]==0:
                    continue
                que.append((new_i,new_j,dis+1))
           
                            
                            

        