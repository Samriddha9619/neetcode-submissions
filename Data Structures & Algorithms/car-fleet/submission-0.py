class Solution:
    def carFleet(self, t: int, p: List[int], s: List[int]) -> int:
        pair=[]
        for pp,ss in zip(p,s):
            pair.append((pp,ss))
        stack =[]
        for pp,ss in sorted(pair)[::-1]:
            res=(t-pp)/ss
            stack.append(res)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)