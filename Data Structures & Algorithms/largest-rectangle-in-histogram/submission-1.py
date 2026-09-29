class Solution:
    def largestRectangleArea(self, he: List[int]) -> int:
        maz=0
        stack=[]
        for i,h in enumerate(he):
            start=i
            while stack and stack[-1][1]>=h:
                index,height=stack.pop()
                maz=max(maz,height*(i-index))
                start=index
            stack.append((start,h))

        for start,h in stack:
            maz=max(maz,h*(len(he)-start))
        return maz