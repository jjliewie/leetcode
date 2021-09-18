class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if j == 0:
                    if grid[i][j] == 1:
                        cnt += 1
                elif grid[i][j-1] != grid[i][j]:
                    cnt += 1

                if j == len(grid[i])-1:
                    if grid[i][j] == 1:
                        cnt += 1

                if i == 0:
                    if grid[i][j] == 1:
                        cnt += 1
                elif grid[i-1][j] != grid[i][j]:
                    cnt += 1

                if i == len(grid)-1:
                    if grid[i][j] == 1:
                        cnt += 1          
                
        return cnt
#         if edge or next to water