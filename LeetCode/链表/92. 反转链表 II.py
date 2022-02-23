'''
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
 

示例 1：


输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
示例 2：

输入：head = [5], left = 1, right = 1
输出：[5]
 

提示：

链表中节点数目为 n
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        ##指针走到
        dump = ListNode(-1)
        dump.next = head
        dump_node = dump
        for _ in range(left - 1):
            dump_node = dump_node.next##固定住需要翻转的链表的前一个节点

        pre_node = dump_node.next
        cur_node = pre_node.next
        for _ in range(right - left):
            pre_node.next = cur_node.next
            cur_node.next = dump_node.next
            dump_node.next = cur_node
            cur_node = pre_node.next
        return dump.next

