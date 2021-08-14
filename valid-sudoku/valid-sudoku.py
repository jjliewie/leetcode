class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range (len(board)):
            row = []
            col = []
            for j in range(len(board[i])):
                if board[i][j] in row:
                    return False
                else:
                    if board[i][j] != '.':
                        row.append(board[i][j])
                
                if board[j][i] in col:
                    return False
                
                else:
                    if board[j][i] != '.':
                        col.append(board[j][i])
        
        square = []
        for i in range(0, len(board), 3):
            for j in range(len(board[i])):
                
                if (j)%3 == 0:
                    square = []
                
                if board[i][j] in square:
                    return False
                if board[i+1][j] in square:
                    return False
                if board[i+2][j] in square:
                    return False
                else:
                    if board[i][j] != '.':
                        square.append(board[i][j])
                    if board[i+1][j] != '.':
                        square.append(board[i+1][j])
                    if board[i+2][j] != '.':
                        square.append(board[i+2][j])
        
        return True