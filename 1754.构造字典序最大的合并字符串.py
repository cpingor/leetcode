#
# @lc app=leetcode.cn id=1754 lang=python3
#
# [1754] 构造字典序最大的合并字符串
#

# @lc code=start
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ''
        while word1 or word2:
            if word1 > word2:
                merge += word1[0]
                word1 = word1[1:]
            else:
                merge += word2[0]
                word2 = word2[1:]
        return merge
# @lc code=end

