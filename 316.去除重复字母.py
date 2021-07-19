#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = []
        for i, v in enumerate(s):
            if v in res:
                continue
            while res and v < res[-1] and res[-1] in s[i:]:
                res.pop()
            res.append(v)
        return ''.join(res)
# @lc code=end

