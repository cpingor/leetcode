#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = {}
        for edge in prerequisites:
            edges.setdefault(edge[1], []).append(edge[0])
        visited = [0] * numCourses

        valid = True
        result = []
        def dfs(v):
            nonlocal valid
            visited[v] = 1
            if v not in edges:
                visited[v] = 2
                result.append(v)
                return
            for node in edges[v]:
                if visited[node] == 1:
                    valid = False
                    return
                elif visited[node] == 0:
                    dfs(node)
                    if not valid:
                        return
            visited[v] = 2
            result.append(v)

        for i in range(numCourses):
            if visited[i] == 0 and valid:
                dfs(i)       

        if not valid:
            return []

        return result[::-1]


# @lc code=end

