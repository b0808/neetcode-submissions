class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)


        def dfs(node,visited,parent=None):
            if visited[node]==1:
                return False
            visited[node]=1
            # print(node)
            for k in adj[node]:
                if k!=parent:
                    if not dfs(k,visited,node):
                        return False
            return True
        visited = [0 for  i in range(n)]
        output= dfs(0,visited)
        if output==False or sum(visited)!=n:
            return False
        return True   