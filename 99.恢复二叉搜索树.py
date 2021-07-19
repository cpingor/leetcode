#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        order  = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            order.append(node.val)
            node = node.right 
        order_s = sorted(order)
        print(order)
        target = []
        for i in range(len(order)):
            if order[i] == order_s[i]:
                continue
            else:
                target.append(i)
            if len(target) == 2:
                break
        print(target)
        dummy = TreeNode(0, root)
        stack = [(dummy, root)]
        parent, node = stack.pop()
        count = 0
        while stack or node:
            while node:
                stack.append((parent, node))
                parent = node
                node = node.left
            parent, node = stack.pop()
            if count in target:
                node.val = order[target[1 - target.index(count)]]
            count += 1
            parent = node
            node = node.right


# @lc code=end

