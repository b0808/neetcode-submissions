class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        
        # print(visted)
        
        final_point  = []
        for r in range(m):
            for q in range(n):
                    visted = [["0" for i in range(n)] for j in range(m)]
                    occ = set()
                    que = deque()
                    visted[r][q] = "1"
                    que.append((r,q))

                    while len(que)!=0:
                        i,j = que.popleft()
                        if i==0 or j==0:
                                occ.add("p")
                        if i==m-1 or j==n-1:
                                occ.add("a")

                        for x,y in d:
                            (new_i,new_j) = (i+x,j+y)

                            if new_i<0 or new_i>=m or new_j<0 or new_j>=n:
                                continue
                            if visted[new_i][new_j]=="1":
                                continue 
                            if heights[i][j]<heights[new_i][new_j]:
                                continue   
                            # print(new_i,new_j)


                            visted[new_i][new_j] = "1"
                            que.append((new_i,new_j))

                    print(set(occ))
                    if occ == {"a","p"}:
                        final_point.append([r,q])
                                # print(new_i,new_j,"new")

        return final_point
        