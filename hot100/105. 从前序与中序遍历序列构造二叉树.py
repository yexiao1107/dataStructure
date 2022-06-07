'''
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

 

示例 1:


输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
示例 2:

输入: preorder = [-1], inorder = [-1]
输出: [-1]
'''


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def build(preStart, preEnd, inStart, inEnd):
            if preStart > preEnd or inStart > inEnd: return None
            root_val = preorder[preStart]
            root = TreeNode(root_val)
            root_index = inorder.index(root_val)
            left_size = root_index - inStart
            root.left = build(preStart + 1, preStart + left_size, inStart, root_index - 1)
            root.right = build(preStart + 1 + left_size, preEnd, root_index + 1, inEnd)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
