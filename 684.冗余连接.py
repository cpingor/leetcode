#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#

# @lc code=start
class UnionFind:
    def __init__(self, M):
        self.father = {}
        for (a, b) in M:
            if a not in self.father:
                self.father[a] = None
            if b not in self.father:
                self.father[b] = None
    
    def find(self, x):
        root = x
        while None != self.father[root]:
            root = self.father[root]
        
        while x != root:
            origin_root = self.father[x]
            self.father[x] = root
            x = origin_root
        
        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
    
    def is_connected(self, x, y):
        return x in self.father and y in self.father and self.find(x) == self.find(y)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(edges)
        for (a, b) in edges:
            if uf.is_connected(a, b):
                return([a, b])
            uf.merge(a, b)
# @lc code=end

