# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftheight=self.mheight(root.left)
        rightheight=self.mheight(root.right)
        dia=leftheight+rightheight

        sub= max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        res=max(dia,sub)
        return res

    def mheight(self, root: Optional[TreeNode]):
            if not root:
                return 0
            return 1 + max(self.mheight(root.left),self.mheight(root.right))