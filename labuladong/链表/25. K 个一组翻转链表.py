'''
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

 

示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
示例 2：



输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
 
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(cur_head, last_node):
            pre, cur = None, cur_head
            while cur != last_node:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre
        if head == None: return None
        a, b = head, head
        for i in range(k):
            if b == None: return head
            b = b.next
        new_head = reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_head