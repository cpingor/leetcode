#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # lst = []
        # while head:
        #     lst.append(head)
        #     head = head.next
        # lst.sort(key=lambda x:x.val)
        # res = ListNode(-1)
        # cur = res
        # for i in range(len(lst)):
        #     cur.next = lst[i]
        #     cur = cur.next
        # cur.next = None
        # return res.next
        def merge_list(head1: ListNode, head2: ListNode) -> ListNode:
            dummy_head = ListNode(0)
            temp, temp1, temp2 = dummy_head, head1, head2
            while temp1 and temp2:
                if temp1.val < temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummy_head.next
        
        # def sort_func(head: ListNode, tail: ListNode) -> ListNode:
        #     if not head:
        #         return head
        #     if head.next == tail:
        #         head.next = None
        #         return head
        #     slow = fast = head
        #     while fast != tail:
        #         slow = slow.next
        #         fast = fast.next
        #         if fast != tail:
        #             fast = fast.next
        #     mid = slow
        #     return merge_list(sort_func(head, mid), sort_func(mid, tail))
        # return sort_func(head, None)

        if not head:
            return head
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        cur_length = 1
        dummy_head = ListNode(0, head)
        while cur_length < length:
            pre, cur = dummy_head, dummy_head.next
            while cur:
                head1 = cur
                for _ in range(1, cur_length):
                    if cur and cur.next:
                        cur = cur.next
                    else:
                        break
                head2 = cur.next
                cur.next = None
                cur = head2
                for _ in range(1, cur_length):
                    if cur and cur.next:
                        cur = cur.next
                    else:
                        break
                succ = None
                if cur:
                    succ = cur.next
                    cur.next = None
                merged = merge_list(head1, head2)
                pre.next = merged
                while pre.next:
                    pre = pre.next
                cur = succ
            cur_length *= 2
        return dummy_head.next

            
# @lc code=end

