class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        i = 0
        j = 1
        res = 0
        while j < len(nums):
            if nums[i] < nums[j]:
                res = max(res, nums[j] - nums[i])
            else:
                i = j
            j += 1
        return res