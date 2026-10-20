class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        cur=[]
        nums.sort()
        def function(s):
            res.append(cur[:])
            for i in range (s,len(nums)):
                if i >s and nums[i]==nums[i-1]:
                    continue
                cur.append(nums[i])
                function(i+1)
                cur.pop()


        function(0)
        return res