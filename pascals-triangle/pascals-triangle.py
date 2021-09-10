class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        result = [[1], [1, 1]]
        
        for i in range(2, numRows):
            result.append([1]*(i+1))
            result[i][0] = 1
            result[i][len(result[i])-1] = 1
            for j in range(1, len(result[i])-1):
                print(len(result[i]))
                result[i][j] = result[i-1][j-1] + result[i-1][j]        
        return result