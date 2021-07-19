#
# @lc app=leetcode.cn id=446 lang=python3
#
# [446] 等差数列划分 II - 子序列
#

# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        diff_dic = [dict() for i in range(n)]
        for j in range(1, n):
            for i in range(j):
                delta = nums[j] - nums[i]
                if delta in diff_dic[j]:
                    diff_dic[j][delta] += 1
                else:
                    diff_dic[j][delta] = 1
                if delta in diff_dic[i]:
                    diff_dic[j][delta] += diff_dic[i][delta]
                    count += diff_dic[i][delta]
        return count
            
# @lc code=end

