class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre=Counter(nums)
        x=sorted(fre,key=lambda x:fre[x])
        return x[-k:]