class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        l,r=0,len(n)-1
        re=[]
        while l<r:
            if n[l]+n[r]==target:
                re.append(l+1)
                re.append(r+1)
                return re
            elif n[l]+n[r]<target:
                l+=1
            elif n[l]+n[r]>target:
                r-=1
        return re
