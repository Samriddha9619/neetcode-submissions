class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dix ={}
        for i,value in enumerate(nums):
            com = target -value
            if com in dix:
                return [dix[com],i]
            dix[value]=i