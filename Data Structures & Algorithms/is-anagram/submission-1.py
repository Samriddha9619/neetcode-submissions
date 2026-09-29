class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=sorted(s)
        b=sorted(t)
        if len(a)!=len(b):
            return False
        for i, j in zip(a,b):
            if i!=j:
                return False
        return True
