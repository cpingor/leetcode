#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
class UnionFind:
    def __init__(self, M):
        self.father = {}
        for i in range(len(M)):
            self.father[i] = None
    
    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]

        while x != root:
            ori_root = self.father[x]
            self.father[x] = root
            x = ori_root
        
        return root
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        print(root_x, root_y)
        if root_x != root_y:
            self.father[root_x] = root_y
    
    def is_connected(self, x, y):
        return x in self.father and y in self.father and self.find(x) == self.find(y)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(isConnected)
        for r in range(len(isConnected)):
            for c in range(len(isConnected)):
                if isConnected[r][c] == 1 and r != c:\
                    uf.union(r, c)
        res = 0
        for key in uf.father:
            if uf.father[key] is None:
                res += 1
        return res


# @lc code=end

