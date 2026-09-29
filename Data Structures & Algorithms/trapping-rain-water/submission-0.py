class Solution:
    def trap(self, nums: List[int]) -> int:
        if not nums: return 0
        res=0
        l,r=0,len(nums)-1
        lm,rm=nums[l],nums[r]
        while l<r :
            if lm<rm:
                l+=1
                lm=max(lm,nums[l])
                res+=lm-nums[l]
            else:
                r-=1
                rm=max(rm,nums[r])
                res+=rm-nums[r]

        return res
        