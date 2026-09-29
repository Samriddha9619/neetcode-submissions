class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        maz=0
        n=len(s)
        for j in range(n):
            while s[j] in seen:
                seen.remove(s[left])
                left+=1

            seen.add(s[j])
            maz=max(maz,j-left+1)
        return maz