#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word = []
        ans = []
        def backtrack(index):
            if index == len(s):
                ans.append(' '.join(word))
            for i in range(1, len(s) + 1):
                if s[index:i] in wordDict:
                    word.append(s[index:i])
                    backtrack(i)
                    word.pop()
        backtrack(0)
        return ans
# @lc code=end

