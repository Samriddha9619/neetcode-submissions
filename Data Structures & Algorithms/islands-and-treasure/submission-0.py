class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf=2147483647
        row,col=len(grid),len(grid[0])
        q=deque()
        visit=set()

        def acell(r,c):
            if (r==row or c==col or min(r,c)<0 or grid[r][c]==-1 or (r,c) in visit):
                return
            visit.add((r,c))
            q.append([r,c])

        for r in range (row):
            for c in range(col):
                if grid[r][c]==0:
                    q.append(([r,c]))
                    visit.add((r,c))

        dist=0
        while q :
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                acell(r+1,c)
                acell(r-1,c)
                acell(r,c+1)
                acell(r,c-1)
            dist+=1

        
                
'''
Islands and Treasure
Medium
Topics
Company Tags
Hints
You are given a 
m
×
n
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
'''