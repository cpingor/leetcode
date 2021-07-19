#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return ' '.join(words) == ' '.join(sorted(words, key=lambda word: [order.index(c) for c in word]))
# @lc code=end

