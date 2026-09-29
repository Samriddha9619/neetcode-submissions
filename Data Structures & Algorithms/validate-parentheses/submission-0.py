class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        maps={')':'(','}':'{',']':'['}
        for char in s :
            if char in maps.values():
                st.append(char)
            else:
                if not st or st[-1]!=maps[char]:
                    return False
                st.pop()
        return not st