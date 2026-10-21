class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Row,Col=len(board),len(board[0])

        def dfs(r,c,i):
            if i==len(word):

                return True

            if r<0 or c<0 or r>=Row or c >=Col or word[i]!=board[r][c] or board[r][c]=='#':
                return False # we check the word[i] to the board letter in the conditions 

            board[r][c]='#'   # after it passes check we can be sure that the letter is that now we replace it with any letter so we dont make it a infinite loop
            res=  dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1) 
            board[r][c]=word[i] 
            return res


        for r in range(Row):
            for c in range(Col):
                if dfs(r,c,0):
                    return True

        return False 