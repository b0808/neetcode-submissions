class Solution:
    def dfs(self,i,visited,path_visited,adj):
        visited[i]=1
        path_visited[i]=1

        for next_node in adj[i]:
            if visited[next_node]==0:
                x = self.dfs(next_node,visited,path_visited,adj)
                if x==False:
                    return False
            if path_visited[next_node]==1:
                return False
        path_visited[i]=0
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)

        for u, v in prerequisites:
            adj[u].append(v)
        visited = [0]*numCourses
        path_visited = [0]*numCourses

        for i in range(0,numCourses):
            if visited[i]==0:
                x = self.dfs(i,visited,path_visited,adj)
                if  x==False:
                    return False
        
        return True