#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pre(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def succ(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not (root.left or root.right):
                return None
            if root.left:
                root.val = self.pre(root)
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = self.succ(root)
                root.right = self.deleteNode(root.right, root.val)
        return root
# @lc code=end

