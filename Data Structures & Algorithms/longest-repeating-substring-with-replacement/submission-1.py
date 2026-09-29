class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dix = {}
        l, res, maxf = 0, 0, 0
        for r in range(len(s)):
            dix[s[r]] = 1 + dix.get(s[r], 0)
            maxf = max(maxf, dix[s[r]])

            while (r - l + 1) - maxf > k:
                dix[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
