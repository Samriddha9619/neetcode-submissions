class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res=['']
        digit_char={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        for i in digits:
            tmp=[]
            for cstr in res:
                for j in digit_char[i]:
                    tmp.append(cstr+j)
            res=tmp

        return res
