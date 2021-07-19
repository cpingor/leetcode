#
# @lc app=leetcode.cn id=814 lang=python3
#
# [814] 二叉树剪枝
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def remove(root):
            if root.left:
                root.left = remove(root.left)
            if root.right:
                root.right = remove(root.right)
            if not root.left and not root.right:
                if root.val == 0:
                    return None
                else:
                    return root
            return root
        return remove(root)

# @lc code=end

