#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1, l2 = len(nums1), len(nums2)
        res = []
        if l1 < l2:
            for i in nums1:
                if i in nums2:
                    nums2.remove(i)
                    res.append(i)
        else:
            for i in nums2:
                if i in nums1:
                    nums1.remove(i)
                    res.append(i)
        return res
# @lc code=end

