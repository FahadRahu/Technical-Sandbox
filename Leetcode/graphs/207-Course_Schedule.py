from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # visitSet = all courses along the curr DFS path
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            # For each item in the list at preMap[crs]
            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            visitSet.remove(crs)
            # Since we know this crs can be visited, it's confirmed True, we can just set it as [] to skip
            # running the work in this function, and just return True in the "if preMap[crs] == []" basecase
            preMap[crs] = []
            return True
        
        # We do range(numCourses) since it's 0 to numCourses, and preMap was made off of range numCourses
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

        # We run through every crs for the "for crs in range(numCourses)" because what if two seperate graphs
        # that aren't related? Like if you had 1 --> 2 and 3 --> 4, these two graphs are not one big graph
        # connected to each other, but are two seperate graphs that don't intersect paths at all.