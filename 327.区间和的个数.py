#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#

# @lc code=start
import bisect
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def cnt(cur, pre, lower, upper):
            # left = bisect.bisect_right(pre, cur - lower)
            # right = bisect.bisect_left(pre, cur - upper)
            l, r = 0, len(pre) - 1
            while l <= r:
                mid = (l + r) // 2
                if cur - pre[mid] < lower:
                    r = mid - 1
                else:
                    l = mid + 1
            temp = l
            l, r = 0, len(pre) - 1
            while l <= r:
                mid = (l + r) // 2
                if cur - pre[mid] > upper:
                    l = mid + 1
                else:
                    r = mid - 1
            return temp - l
            # return left - right

        cur = 0
        ans = 0
        pre = []
        for i in nums:
            cur += i
            # pre.append(cur)
            if lower <= cur <= upper:
                ans += 1
            ans += cnt(cur, pre, lower, upper)
            bisect.insort(pre, cur)
            # pre.append(cur)
        return ans
        # summ = 0
        # prefix = [0]
        # n = len(nums)
        # for i in nums:
        #     summ += i
        #     prefix.append(summ)
        # temp = []
        # ans = 0
        # for i in prefix[::-1]:
        #     left = bisect.bisect_left(temp, i + lower)
        #     right = bisect.bisect_right(temp, i + upper)
        #     ans += (right - left)
        #     bisect.insort(temp, i)
        # return ans
        
# @lc code=end

