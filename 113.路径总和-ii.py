#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def dfs(root, path, current_sum):
            if current_sum == targetSum and not root.left and not root.right:
                ans.append(path)
            else:
                if root.left:
                    dfs(root.left, path + [root.left.val], current_sum + root.left.val)
                if root.right:
                    dfs(root.right, path + [root.right.val], current_sum + root.right.val)
        dfs(root, [root.val], root.val)
        return ans
# @lc code=end

