class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        n=len(h)
        stack=[]
        leftmost =[-1]*n
        rightmost=[n]*n
        for i in range(n):
            while stack and h[stack[-1]]>=h[i]:
                stack.pop()
            if stack:
                leftmost[i]=stack[-1]
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and h[stack[-1]]>=h[i]:
                stack.pop()
            if stack:
                rightmost[i]=stack[-1]
            stack.append(i)

        maxa=0
        for i in range(n):
            leftmost[i]+=1
            rightmost[i]-=1
            maxa=max(maxa,h[i]*(rightmost[i]-leftmost[i]+1))

        return maxa