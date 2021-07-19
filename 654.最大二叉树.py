#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        max = 0
        for i in range(len(nums)):
            if nums[i] > nums[max]:
                max = i
        return TreeNode(nums[max], self.constructMaximumBinaryTree(nums[:max]), self.constructMaximumBinaryTree(nums[max + 1:]))

# @lc code=end

