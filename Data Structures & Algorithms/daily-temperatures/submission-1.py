class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(nums)
        for i,t in enumerate(nums):
            while stack and t> stack[-1][1]:
                stackind,stackt=stack.pop()
                res[stackind]=i-stackind
            stack.append((i,t))
        return res