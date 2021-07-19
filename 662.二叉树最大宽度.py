#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
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
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        stack = deque([(root, 1, 1)])
        ans = 0
        min_index = 1
        depth = 1
        while stack:
            node = stack.popleft()
            if node[0]:
                stack.append((node[0].left, node[1] * 2, node[2] + 1))
                stack.append((node[0].right, node[1] * 2 + 1, node[2] + 1))
                if node[2] != depth:
                    depth += 1
                    min_index = node[1]
                ans = max(ans, node[1] - min_index + 1)
        return ans


# @lc code=end

