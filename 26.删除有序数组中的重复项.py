#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        res = 1
        a = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == a:
                nums.pop(i)
            else:
                a = nums[i]
                res += 1
        return res
# @lc code=end

