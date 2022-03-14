'''
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

 

示例 1:


输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
示例 2:

输入: preorder = [-1], inorder = [-1]
输出: [-1]
 

提示:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder 和 inorder 均 无重复 元素
inorder 均出现在 preorder
preorder 保证 为二叉树的前序遍历序列
inorder 保证 为二叉树的中序遍历序列

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
            node = TreeNode(root_val)
            index = 0
            for i in range(inStart, inEnd + 1):
                if inorder[node] == root_val:
                    index = i
                    break
            left_size = index - inStart
            node.left = build(preStart + 1, preStart + left_size, inStart, index - 1)
            node.right = build(preStart + 1 + left_size, preEnd, index + 1, inEnd)
            return node

        root = build(0, len(preorder) - 1, 0, len(inorder) - 1)
        return root
