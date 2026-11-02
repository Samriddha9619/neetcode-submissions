class Solution:
    def findOrder(self, course: int, prereq: List[List[int]]) -> List[int]:
        cycle=set()
        visit=set()
        output=[]
        premap={i:[] for i in range(course)}

        for crs,pre in prereq:
            premap[crs].append(pre)

        def dfs(crs):

            if crs in cycle:
                return False
            if crs in visit:
                return True 

            cycle.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            #don't really need visit but hashset is more efficient to look into for the condition
            # if crs in visit: return True 
            visit.add(crs)
            output.append(crs) 
            return True

        for c in range(course):
            if not dfs(c):
                return []

        return output