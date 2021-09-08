#
# @lc app=leetcode.cn id=1202 lang=python3
#
# [1202] 交换字符串中的元素
#

# @lc code=start
class UnionFind:
    def __init__(self, pairs):
        self.father = {}
        for a, b in pairs:
            if a not in self.father:
                self.father[a] = None
            if b not in self.father:
                self.father[b] = None
    
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
        # print(self.find(x), self.father[self.find(x)], self.find(y))
            self.father[root_x] = root_y
        # print(self.father)

    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(pairs)
        alphabet = set()
        for a, b in pairs:
            alphabet.add(a)
            alphabet.add(b)
            uf.union(a, b)
        temp = {}
        res = list(s)
        for a in alphabet:
            t = uf.find(a)
            if t not in temp:
                temp[t] = [a]
            else:
                temp[t].append(a)

        for key in temp:
            tmp = []
            for k in temp[key]:
                tmp.append(res[k])
            tmp.sort()
            for i, k in enumerate(sorted(temp[key])):
                res[k] = tmp[i]
        return ''.join(res)

# @lc code=end

