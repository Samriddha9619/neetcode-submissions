class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        r=[]
        for ch in s:
            if ch.isalnum():
                ch=ch.lower()
                r.append(ch)
        s=''.join(r)
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True