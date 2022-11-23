class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        st = set()
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                cell = board[i][j]
                if cell == '.':
                    continue
                boxNum = 3*(i//3) + j//3
                row = f"row : {i}, value: {cell}"
                col = f"col : {j}, value: {cell}"
                box = f"box : {boxNum}, value: {cell}"
                if row in st or col in st or box in st:
                    return False
                st.add(row)
                st.add(col)
                st.add(box)
        return True
                
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         cols = collections.defaultdict(set)
#         rows = collections.defaultdict(set)
#         squares = collections.defaultdict(set)  # key = (r /3, c /3)

#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == ".":
#                     continue
#                 if (
#                     board[r][c] in rows[r]
#                     or board[r][c] in cols[c]
#                     or board[r][c] in squares[(r // 3, c // 3)]
#                 ):
#                     return False
#                 cols[c].add(board[r][c])
#                 rows[r].add(board[r][c])
#                 squares[(r // 3, c // 3)].add(board[r][c])

#         return True


# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rowSet = [set() for _ in range(len(board))]
#         colSet = [set() for _ in range(len(board))]
#         squareSet = [set() for _ in range(len(board))]
        
#         for r in range(len(board)):
#             for c in range(len(board[0])):
                
#                 if board[r][c] == '.':
#                     continue
                
#                 squareRow = r//3
#                 squareCol = c//3
#                 squarePosition = squareRow * 3 + squareCol
                
#                 if board[r][c] in rowSet[r] or board[r][c] in colSet[c] or board[r][c] in squareSet[squarePosition]:
#                     return False
                
#                 rowSet[r].add(board[r][c])
#                 colSet[c].add(board[r][c])
#                 squareSet[squarePosition].add(board[r][c])
        
#         return True
































                    
                    
            