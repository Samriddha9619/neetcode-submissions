class Solution:
    def canFinish(self, course: int, prereq: List[List[int]]) -> bool:
        visit=set()
        premap={ i:[] for i in range(course)}
        for crs,pre in prereq:
            premap[crs].append(pre)

        def dfs(crs):
            if crs in visit:
                return False

            if premap[crs]==[]:
                return True

            visit.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False

            visit.remove(crs)
            premap[crs]=[]
            return True

        for c in range(course):
            if not dfs(c):
                return False

        return True 