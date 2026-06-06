from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        print(m,n)
        mint = 0
        que = deque()
        mat = [row[:] for row in grid]
        fresh = 0
        


        d = [(-1,0),(1,0),(0,1),(0,-1)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 2:
                    que.append((i,j))
                if mat[i][j] == 1:
                    fresh = fresh+1
        if fresh ==0:
            return 0

        while len(que)>0 and fresh>0:
            mint = mint +1
            # print(mint,"min")
            # print(que,"que")
            
            for q in range(len(que)):
                i,j = que.popleft()
                for x,y in d:
                    (new_i,new_j) = (i+x,j+y)
                    print(new_i,new_j,"new",x,y,"old",i,j) 
                    if new_i<0 or new_i>=m or new_j<0 or new_j>=n:
                        # print("yes")
                        continue
                    if mat[new_i][new_j] == 0 or mat[new_i][new_j]== 2:
                        continue
                    
                    # print(new_i,new_j,"rot")
                    mat[new_i][new_j] =2
                    que.append((new_i,new_j))
                    fresh = fresh -1
                    # print(fresh,"fresh")
                    if fresh == 0:
                        return mint
            
        return -1





        