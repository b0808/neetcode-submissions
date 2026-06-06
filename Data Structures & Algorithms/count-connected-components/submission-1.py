class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        def dfs(node,visited):
            if visited[node]==1:
                return
            visited[node]=1
            # print(node)
            for k in adj[node]:
                dfs(k,visited)
        m = []
        visited = [0 for  i in range(n)]
        count = 0
        for i in range(n): 
            if visited[i]==0:
                count = count+1
                dfs(i,visited)
        return count
            

