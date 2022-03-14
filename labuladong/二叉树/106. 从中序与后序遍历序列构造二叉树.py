'''
给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。

 

示例 1:


输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]
示例 2:

输入：inorder = [-1], postorder = [-1]
输出：[-1]

'''


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        def build(inStart, inEnd, postStart, postEnd):
            if inStart > inEnd or postStart > postEnd: return None
            index = 0
            node = TreeNode(postorder[postEnd])
            for i in range(inStart, inEnd + 1):
                if inorder[i] == postorder[postEnd]:
                    index = i
                    break
            left_size = index - inStart
            node.left = build(inStart, index - 1, postStart, postStart + left_size - 1)
            node.right = build(index + 1, inEnd, postStart + left_size, postEnd - 1)
            return node

        root = build(0, len(inorder) - 1, 0, len(postorder - 1))
        return root
