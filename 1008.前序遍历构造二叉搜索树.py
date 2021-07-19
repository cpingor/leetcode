#
# @lc app=leetcode.cn id=1008 lang=python3
#
# [1008] 前序遍历构造二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        for i in range(len(preorder)):
            if preorder[i] > preorder[0]:
                break
        else:
            i = len(preorder)
        root.left = self.bstFromPreorder(preorder[1: i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
# @lc code=end

