class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(path,used):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i]=True
                    dfs(path,used)
                    path.pop()
                    used[i]=False


        dfs([],[False]*len(nums))
        return res