class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        
        n = len(image)
        m = len(image[sr])
        
        visit = []
        
        def bfs(u, t):
            if image[sr][sc] == image[u][t]:
                if (u, t) not in visit:
                    visit.append((u, t))
                    
                    if u > 0:
                        bfs(u-1, t)
                    if u < n-1:
                        bfs(u+1, t)
                    if t > 0:
                        bfs(u, t-1)
                    if t < m-1:
                        bfs(u, t+1)
                
        bfs(sr, sc)
        
        for i in visit:
            image[i[0]][i[1]] = newColor
            
        return image
            
        