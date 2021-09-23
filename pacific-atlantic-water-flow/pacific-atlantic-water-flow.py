class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = []
        atlantic = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    pacific.append((i, j))
                if i == len(heights)-1 or j == len(heights[0])-1:
                    atlantic.append((i, j))
        
        pacific_grid = []
        atlantic_grid = []
        def dfs(i, j, grid): 
            if (i, j) not in grid:
                grid.append((i, j))
                
                if i-1 >= 0:
                    if heights[i-1][j] >= heights[i][j]:
                        dfs(i-1, j, grid)
                if j-1 >= 0:
                    if heights[i][j-1] >= heights[i][j]:
                        dfs(i, j-1, grid)
                if i+1 < len(heights):
                    if heights[i+1][j] >= heights[i][j]:
                        dfs(i+1, j, grid)
                if j+1 < len(heights[0]):
                    if heights[i][j+1] >= heights[i][j]:
                        dfs(i, j+1, grid)
        
        result = []
        for i in pacific:
            dfs(i[0], i[1], pacific_grid)
        for i in atlantic:
            dfs(i[0], i[1], atlantic_grid)
        
        for k in pacific_grid:
            if k in atlantic_grid:
                result.append(k)
                
        return result