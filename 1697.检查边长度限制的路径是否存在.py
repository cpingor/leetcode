#
# @lc app=leetcode.cn id=1697 lang=python3
#
# [1697] 检查边长度限制的路径是否存在
#

# @lc code=start
from typing import Union


class UnionFind:
    def __init__(self):
        self.father = {}

    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
        
        while x != root:
            ori = self.father[x]
            self.father[x] = root
            x = ori

        return x
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
    
    def connected(self, x, y):
        return x in self.father and y in self.father and self.find(x) == self.find(y)

    def add(self, x):
        if x not in self.father:
            self.father[x] = None


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind()
        for i in range(n):
            uf.add(i)
        res = [False] * len(queries)
        queries_index = sorted(range(len(queries)), key=lambda x: queries[x][2], reverse=True)
        for a, b, val in sorted(edgeList, key=lambda x: x[2]):
            while queries_index:
                i = queries_index[-1]
                p, q, limit = queries[i]
                if val >= limit:
                    queries_index.pop()
                    if uf.connected(p, q):
                        res[i] = True
                else:
                    break
            else:
                return res
            uf.union(a, b)
        for i in queries_index:
            p, q, _ = queries[i]
            if uf.connected(p, q):
                res[i] = True
        return res
                
# @lc code=end

