'''
给你一个二叉树的根节点 root ， 检查它是否轴对称。

 

示例 1：


输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：


输入：root = [1,2,2,null,3,null,3]
输出：false

'''


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def checkout(left, right):
            if left == None or right == None: return left == right
            if left.val != right.val: return False
            return checkout(left.right, right.left) and checkout(left.left, right.right)

        if root == None: return True
        return checkout(root.left, root.right)
