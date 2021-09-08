#
# @lc app=leetcode.cn id=990 lang=python3
#
# [990] 等式方程的可满足性
#

# @lc code=start
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x not in father:
                father[x] = x
                return x
            while x != father[x]:
                x = father[x]
            return x
        
        def union(x, y):
            father[find(x)] = find(y)
        
        def connected(x, y):
            return find(x) == find(y)
        
        father = {}
        for e in equations:
            a = e[0]
            b = e[-1]
            if '!' not in e:
                union(a, b)
        for e in equations:
            a = e[0]
            b = e[-1]
            if '!' in e:
                if connected(a, b):
                    return False
        return True



# @lc code=end

