class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        c,cc,ccc=0,0,0
        for i in range(len(nums)):
            if nums[i]==0:
                c+=1
            if nums[i]==1:
                cc+=1
            if nums[i]==2:
                ccc+=1
        for i in range(len(nums)):
            if c!=0:
                nums[i]=0
                c-=1
            elif cc!=0:
                nums[i]=1
                cc-=1
            elif ccc!=0:
                nums[i]=2
                ccc-=1




        