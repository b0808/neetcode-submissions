class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        d = [(0,1),(1,0),(-1,0),(0,-1)]

        p = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
        a = [(m-1, j) for j in range(n)] + [(i, n-1) for i in range(m)]


        def bfs(p):
            que = deque()
            visit = [[0 for j in range(n)] for i in range(m)]
            for i,j in p:
                if visit[i][j]==1:
                    continue 
                visit[i][j]=1
                que.append((i,j))
                while len(que)!=0:
                    i,j = que.popleft()
                    for x,y in d:
                        new_i,new_j = x+i,y+j
                        if new_i<0 or new_i>m-1 or new_j<0 or new_j>n-1:
                            continue 
                        if visit[new_i][new_j]==1:
                            continue 
                        if heights[new_i][new_j]<heights[i][j]:
                            continue 
                        que.append((new_i,new_j))
                        visit[new_i][new_j] = 1

            return visit
        visit_1 = bfs(p)
        visit_2 = bfs(a)
        common =[]
        for i in range(m):
            for j in range(n):
                if visit_1[i][j]==1  and visit_2[i][j]==1:
                    common.append([i,j])
        return common
                





