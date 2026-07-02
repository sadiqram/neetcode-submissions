class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        tbyt = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                
                if (board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in tbyt[row//3,col//3]):
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                tbyt[row//3,col//3].add(board[row][col])
        return True