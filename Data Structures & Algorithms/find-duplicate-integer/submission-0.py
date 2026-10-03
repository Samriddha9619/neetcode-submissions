class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l=0
        r=1
        seen={}
        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            else:
                seen[nums[i]]=True
        return 