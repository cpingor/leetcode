#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l = len(s)
        m = len(words)
        n = len(words[0])
        res = []
        for index in range(l - m * n + 1):
            if s[index : index + n] in words:
                temp = [s[index:][i : i + n] for i in range(0, m * n, n)]
                if list(sorted(words)) == list(sorted(temp)):
                    res.append(index)
        return res




# @lc code=end

