#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
# https://leetcode-cn.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (46.99%)
# Likes:    165
# Dislikes: 0
# Total Accepted:    32.5K
# Total Submissions: 68.9K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA
# 中的重复序列有时会对研究非常有帮助。
# 
# 编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
# 
# 
# 示例 2：
# 
# 
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# s[i] 为 'A'、'C'、'G' 或 'T'
# 
# 
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        temp = {}
        for i in range(len(s) - 9):
            tem = s[i:i + 10]
            if tem in temp:
                temp[tem] += 1
            else:
                temp[tem] = 1
        for i, v in temp.items():
            if v > 1:
                res.append(i)
        return res
# @lc code=end

