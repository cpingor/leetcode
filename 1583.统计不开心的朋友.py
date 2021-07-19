#
# @lc app=leetcode.cn id=1583 lang=python3
#
# [1583] 统计不开心的朋友
#

# @lc code=start
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        l = len(pairs)
        count = set()
        if l == 1:
            return 0
        for i in range(l):
            a, b = pairs[i][0], pairs[i][1]
            for j in range(i+1, l):
                c, d = pairs[j][0], pairs[j][1]
                if preferences[a].index(b) > preferences[a].index(c) and preferences[c].index(a) < preferences[c].index(d):
                    count.add(a)
                    count.add(c)
                if preferences[a].index(b) > preferences[a].index(d) and preferences[d].index(a) < preferences[d].index(c):
                    count.add(a)
                    count.add(d)
                if preferences[b].index(a) > preferences[b].index(c) and preferences[c].index(b) < preferences[c].index(d):
                    count.add(b)
                    count.add(c)
                if preferences[b].index(a) > preferences[b].index(d) and preferences[d].index(b) < preferences[d].index(c):
                    count.add(b)
                    count.add(d)
        return len(count)
        
# @lc code=end

