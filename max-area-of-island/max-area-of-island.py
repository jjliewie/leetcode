class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = []
        
        def function(row, col):
            if row > len(grid)-1 or row < 0 or col > len(grid[0])-1  or col < 0:
                return 0
            if grid[row][col] == 1:
                grid[row][col] = 0
                return 1 + function(row-1, col) + function(row+1, col) + function(row, col-1) + function(row, col+1)
            else:
                return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                result.append(function(i, j))
        return max(result)