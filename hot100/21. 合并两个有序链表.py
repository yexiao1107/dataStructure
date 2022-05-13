'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dump_node = ListNode(-1)
        head = dump_node
        while list1 and list2:
            list1_val = list1.val
            list2_val = list2.val
            if list1_val <= list2_val:
                head.next = ListNode(list1_val)
                list1 = list1.next
            else:
                head.next = ListNode(list2_val)
                list2 = list2.next
            head = head.next
        if list1:
            head.next = list1
        if list2:
            head.next = list2
        return dump_node.next
