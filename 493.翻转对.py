#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def bisect(nums, num):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + r >> 1
                if nums[mid] <= num:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        temp = []
        ans = 0
        for num in nums:
            insinx = bisect(temp, 2 * num)
            ans += len(temp) - insinx
            ix = bisect(temp, num)
            temp.insert(ix, num)
        return ans


# @lc code=end

