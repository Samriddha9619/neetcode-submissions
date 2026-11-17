class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        s=[]
        for i in range(len(nums)):
            if nums[i] in s:
                continue
            else:
                s.append(nums[i])
        for i in range(len(s)):
            nums[i]=s[i]
        return len(s)