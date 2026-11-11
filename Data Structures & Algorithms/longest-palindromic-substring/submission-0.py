class Solution:
    def longestPalindrome(self, s: str) -> str:
        residx=0
        reslen=0
        def check(l,r):
            nonlocal residx,reslen
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)> reslen:
                    residx=l
                    reslen=r-l+1
                l-=1
                r+=1
        for i in range (len(s)):
            check(i,i)
            check(i,i+1)

        return s[residx:residx+reslen]
        

        