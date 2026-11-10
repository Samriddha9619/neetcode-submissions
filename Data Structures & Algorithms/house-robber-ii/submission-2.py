class Solution:

    def rob(self, nums: List[int]) -> int:
        if not nums:
                return 0
        if len(nums)==1:
                return nums[0]
        def helper(nums):
            
            n=len(nums)
            dix={}
            def rec(i):
                if i>=n:
                    return 0
                if i in dix:
                    return dix[i]
                dix[i]= max(rec(i+1),nums[i]+rec(i+2))
                return dix[i]
            return rec(0)
        return max(helper(nums[1:]),helper(nums[:-1]))