class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            new=[]
            for subset in res:
                new.append(subset+[num])
            res+= new

        return res