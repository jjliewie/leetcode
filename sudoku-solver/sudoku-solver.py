class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        def check_finish(path):
            for i in range(9):
                for j in range(9):
                    if path[i][j] =='.':
                        return False
            return True
        def col_safe(a, b, c):
            for i in range(9):
                if c in self.board[a][i]:
                    return False
 
            return True
 
        def row_safe(a, b, c):
            for i in range(9):
                if c == self.board[i][b]:
                    return False
 
            return True
 
        def box_safe(r, c, item):
            for k in range(3):
                for l in range(3):
                    n_r,n_c = r - (r%3) + k, c -(c%3) + l
                    if self.board[n_r][n_c] == item:
                        return False
            return True        
 
        def dfs(row,col):
            if check_finish(self.board):
                return True
            if self.board[row][col] != '.':
                if row < 8 :
                    return dfs(row+1,col)
                elif row == 8 :
                    return dfs(0,col+1)
            else : 
                for i in range(1,10):
                    if row_safe(row,col,str(i)) and col_safe(row,col,str(i)) and box_safe(row,col,str(i)):
                        self.board[row][col] = str(i)                
                        if dfs(row,col):
                            return True
                    self.board[row][col] = "."
 
 
        dfs(0,0)
 
        return self.board
        
        
        
#         def col_safe(board, a, b, c):
#             if c in board[a]:
#                 return False
            
#             return True
            
#         def row_safe(board, a, b, c):
#             for i in range(len(board)):
#                 if c == board[i][b]:
#                     return False
                
#             return True
                
#         def box_safe(board, a, b, c):
#             p = a % 3
#             q = b % 3
            
#             for i in range(a-p, a-p+3):
#                 for j in range(b-q, b-q+3):
#                     if board[i][j] == c:
#                         return False
#             return True
            
# #         def safe(board, a, b):
            
# #             col_check = []
# #             row_check = []
# #             box_check = []
            
            
            
# #             k = board[a][b]
            
# #             for i in board[a]:
# #                 if i in k:
# #                     k.remove(i)
        
# #             for i in range(len(board)):
# #                 if board[i][b] in k:
# #                     k.remove(board[i][b])
                    
# #             p = a % 3
# #             q = b % 3
            
# #             for i in range(a-p, a-p+3):
# #                 for j in range(b-q, b-q+3):
# #                     if board[i][j] in k:
# #                         k.remove(board[i][j])
# #             return k
        
#         for i in range(len(board)):
#             for j in range(len(board[i])):
#                 if board[i][j] == ".":
#                     temp = ""
#                     for k in range(1, 10):
#                         if col_safe(board, i, j, str(k)) and row_safe(board, i, j, str(k)) and box_safe(board, i, j, str(k)):
#                             temp += str(k)
#                     if len(temp) == 1:
#                         board[i][j] = temp[0]
                        
#         use = True
#         for i in range(len(board)):
#             for j in range(len(board[i])):
#                 if board[i][j] == ".":
#                     use = False
#         if use:
#             return board
#         else:
#             return self.solveSudoku(board)