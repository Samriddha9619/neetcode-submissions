class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dix={}
        for i,val in enumerate(nums):
            if val in dix:
                return True
            else :
                dix[val]=i
        return False