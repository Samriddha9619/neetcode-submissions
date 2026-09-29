from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
                    
        for s in strs:
            sort_s = "".join(sorted(s))                             
            res[sort_s].append(s)
        return list(res.values())