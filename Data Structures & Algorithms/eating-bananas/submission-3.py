class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,high=1,max(piles)
        res=0
        def answer(piles,mid):
            hours=0
            for i in piles:
                if i%mid==0:
                    hours=(hours)+i//mid
                else:
                    hours=(hours)+i//mid+1
            return hours
        while l<=high:
            mid=(l+high)//2
            if answer(piles,mid)<=h:
                res=mid
                high=mid-1
            else:
                l=mid+1
        return res
        