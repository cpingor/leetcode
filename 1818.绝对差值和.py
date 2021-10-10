#
# @lc app=leetcode.cn id=1818 lang=python3
#
# [1818] 绝对差值和
#

# @lc code=start
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        def binary_search(nums1, target):
            l = 0
            n = len(nums1)
            if target > nums1[-1]:
                return n - 1
            r = len(nums1)
            while l <= r:
                mid = l + r >> 1
                if nums1[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            if l > 0 and abs(nums1[l] - target) > abs(nums1[l - 1] - target):
                l -= 1
            return l
        ans = 0
        max_diff = 0
        temp = nums1.copy()
        temp.sort()
        for i in range(len(nums1)):
            t = abs(nums1[i] - nums2[i])
            max_diff = max(max_diff, t - abs(temp[binary_search(temp, nums2[i])] - nums2[i]))
            ans += t
        return (ans - max_diff) % (10 ** 9 + 7)
# @lc code=end

