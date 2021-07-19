#
# @lc app=leetcode.cn id=1346 lang=python3
#
# [1346] 检查整数及其两倍数是否存在
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort(key=abs)
        l = len(arr)
        for i in range(l):
            for j in range(i + 1, l):
                if arr[j] == 2 * arr[i]:
                    return True
                # if arr[j] > 2 * arr[i]:
                #     continue
        return False
# @lc code=end

