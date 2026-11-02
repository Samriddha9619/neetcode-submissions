class Solution:
    def findOrder(self, course: int, prereq: List[List[int]]) -> List[int]:
        cycle=set()
        output=[]
        premap={i:[] for i in range(course)}

        for crs,pre in prereq:
            premap[crs].append(pre)

        def dfs(crs):

            if crs in cycle:
                return False
            if crs in output:
                return True 

            cycle.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            output.append(crs)
            return True

        for c in range(course):
            if not dfs(c):
                return []

        return output