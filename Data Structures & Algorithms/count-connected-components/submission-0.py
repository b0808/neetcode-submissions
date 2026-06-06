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
        for i in range(n):
            
            visited = [0 for  i in range(n)]
            dfs(i,visited)
            print(visited)
            if visited not in m:
                m.append(visited)
            print(m)
        return len(m)

