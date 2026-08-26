class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for row in range(n)]
        posDiag = set()
        negDiag = set()
        cols = set()
        res = [] 
        # Bounding function, not in same row/col/diagonal

        def dfs(r):
            # base case/exit condition
            if r == n:
                board_copy = ["".join(row) for row in board]
                res.append(board_copy)
                return

            
            # if position is in same row/col/diagon as another queen
            for c in range(n):
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                dfs(r+1)
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."

        dfs(0)
        return res
                
        