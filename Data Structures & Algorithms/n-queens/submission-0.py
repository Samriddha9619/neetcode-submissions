class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col,posdig,negdig=set(),set(),set()
        res=[]
        board=[['.'] *n for i in range(n)]
        def back(r):
            if r==n:
                copy=["".join(i) for i in board ]
                res.append(copy)
                return 
            for c in range(n):
                if c in col or (r+c) in posdig or (r-c) in negdig:
                    continue
                col.add(c)
                posdig.add(r+c)
                negdig.add(r-c)
                board[r][c]="Q"
                back(r+1)
                col.remove(c)
                posdig.remove(r+c)
                negdig.remove(r-c)
                board[r][c]="."
        back(0)
        return res
