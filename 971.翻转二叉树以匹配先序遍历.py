#
# @lc app=leetcode.cn id=971 lang=python3
#
# [971] 翻转二叉树以匹配先序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        stack = []
        i = 0
        res = []
        cur = (root, 0)
        while stack or cur[0]:
            if cur[0]:
                if cur[0].val == voyage[i]:
                    stack.append((cur[0].right, cur[0].val))
                    cur = (cur[0].left, cur[0].val)
                    i += 1
                else:
                    if stack:
                        node = stack.pop()
                    else:
                        return [-1]
                    stack.append((cur[0], cur[1]))
                    if cur[1] in res:
                        return [-1]
                    cur = node
                    res.append(node[1])
            else:
                cur = stack.pop()
        return res

            
# @lc code=end

