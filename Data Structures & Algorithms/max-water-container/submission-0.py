class Solution:
    def maxArea(self, nums: List[int]) -> int:
        res=0
        l,r=0,len(nums)-1
        while l<r:
            area = (r-l)*min(nums[l],nums[r])
            res=max(res,area)
            if nums[l]<nums[r]:
                l+=1
            else:
                r-=1
                

        return res