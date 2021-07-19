#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        set1 = set(s1)
        set2 = set(s2)
        res = set1 ^ set2
        for word in list(res):
            if s1.count(word) > 1 or s2.count(word) > 1:
                res.remove(word)
        return list(res)
# @lc code=end

