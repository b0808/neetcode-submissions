from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        land_point = []
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        visted = [["0" for i in range(n)] for j in range(m)]
        # print(visted)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    land_point.append([i,j])
        que = deque()
        
        num = 0
        print(land_point)
        for [i,j] in land_point:
            # print(visted,"visit")
            # print(grid,"grid")
            if visted[i][j] == "1":
                    continue
            visted[i][j] = "1"
            num = num+1
            # print(num,"num")
            que.append((i,j))

            while len(que)!=0:
                i,j = que.popleft()

                for x,y in d:
                    (new_i,new_j) = (i+x,j+y)

                    if new_i<0 or new_i>=m or new_j<0 or new_j>=n:
                        continue
                    if grid[new_i][new_j] == "1" and visted[new_i][new_j] == "0":
                        visted[new_i][new_j] = "1"
                        que.append((new_i,new_j))
                        # print(new_i,new_j,"new")

        return num

            


        


        