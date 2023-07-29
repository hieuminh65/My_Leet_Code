# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # return the max length of depest children of every node
        res = 0
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            diameter = left + right + 2
            nonlocal res
            res = max(res, diameter)
            return 1 + max(left, right)
        dfs(root)
        return res
