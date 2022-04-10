'''
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

 

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

 

注意：两结点之间的路径长度是以它们之间边的数目表示。
'''
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxdepth(node):
            if node == None: return 0
            left = maxdepth(node.left)
            right = maxdepth(node.right)
            self.res = max(left + right, self.res)
            return max(left, right) + 1
        ##思路就是后序遍历，左右子树的路径和最大
        self.res = 0
        if root == None: return 0
        maxdepth(root)
        return self.res
