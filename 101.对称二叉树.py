# @before-stub-for-debug-begin
from python3problem101 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs_pre(root):
            queue = collections.deque([root])
            ans = []
            while queue:
                node = queue.popleft()
                if not node: 
                    ans.append(None)
                    continue
                else:
                    ans.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            return ans
        
        def dfs_post(root):
            queue = collections.deque([root])
            ans = []
            while queue:
                node = queue.popleft()
                if not node:
                    ans.append(None)
                    continue
                else:
                    ans.append(node.val)
                    queue.append(node.right)
                    queue.append(node.left)
            return ans
        ans1 = dfs_pre(root)
        ans2 = dfs_post(root)
        for i in range(len(ans1)):
            if ans1[i] != ans2[i]:
                return False
        return True

        
# @lc code=end

