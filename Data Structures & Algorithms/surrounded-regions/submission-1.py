class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row,col=len(board),len(board[0])

        def cap(r,c):
            if r<0 or r==row or c<0 or c==col or board[r][c]!='O':
                return 
            board[r][c]='T'
            cap(r+1,c)
            cap(r-1,c)
            cap(r,c+1)
            cap(r,c-1)

        for r in range(row):
            if board[r][0]=='O':
                cap(r,0)
            if board[r][col-1]=='O':
                cap(r,col-1)
        
        for c in range(col):
            if board[0][c]=='O':
                cap(0,c)
            if board[row-1][c]=='O':
                cap(row-1,c)

        for r in range(row ):
            for c in range(col):
                if board[r][c]=='O':
                    board[r][c]='X'
                if board[r][c]=='T':
                    board[r][c]='O'