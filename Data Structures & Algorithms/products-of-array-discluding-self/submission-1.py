class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #saw the hint this is literally output= {prefix1*suffix_n,prefix2*suffi_xn-1}
        output=[1]*len(nums)
        pre=1
        for i in range(len(nums)):
            output[i]*=pre
            pre*=nums[i]

        suf=1
        for i in range(len(nums)-1,-1,-1):
            output[i]*=suf
            suf*=nums[i]
        return output
