class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        old_color = image[sr][sc]
        if image[sr][sc] == color:
            return image
        d = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(i,j):
            image[i][j] = color
            for x,y in d:
                (new_i,new_j) = (i+x,j+y)
                print(new_i,new_j)
                if new_i<0 or new_i>=m or new_j<0 or new_j>=n:
                    continue 
                if image[new_i][new_j] == color or image[new_i][new_j] != old_color:
                    continue
                dfs(new_i,new_j)
        dfs(sr,sc)
        return image
'''        
1 1 1 
1 2 0
1 0 1
'''