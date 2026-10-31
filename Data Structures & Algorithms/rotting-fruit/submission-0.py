class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row,col=len(grid),len(grid[0])
        q=deque()
        
        fresh=0

        def other_cell(r,c):
            nonlocal fresh 
            if (r==row or r<0 or c<0 or c==col  or grid[r][c]==0 or grid[r][c]==2 ):
                return
            q.append([r,c])
            grid[r][c]=2
            fresh-=1

        for r in range(row):
            for c in range (col):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])

        time=0
        while fresh >0 and q:
            for i in range(len(q)):
                r,c=q.popleft()
                other_cell(r+1,c)
                other_cell(r-1,c)
                other_cell(r,c+1)
                other_cell(r,c-1)
            time+=1

        return time if fresh==0 else -1
            