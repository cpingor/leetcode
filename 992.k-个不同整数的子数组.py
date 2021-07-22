#
# @lc app=leetcode.cn id=992 lang=python3
#
# [992] K 个不同整数的子数组
#

# @lc code=start
import collections
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        num1, num2 = collections.Counter(), collections.Counter()
        tot1 = tot2 = 0
        left1 = left2 = 0
        res = 0

        for num in nums:
            if num1[num] == 0:
                tot1 += 1
            num1[num] += 1
            if num2[num] == 0:
                tot2 += 1
            num2[num] += 1
            
            while tot1 > k:
                num1[nums[left1]] -= 1
                if num1[nums[left1]] == 0:
                    tot1 -= 1
                left1 += 1
            while tot2 > k - 1:
                num2[nums[left2]] -= 1
                if num2[nums[left2]] == 0:
                    tot2 -= 1
                left2 += 1
            
            res += left2 - left1
        
        return res
# @lc code=end

