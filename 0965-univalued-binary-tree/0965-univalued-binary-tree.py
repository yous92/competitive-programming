# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, val: int) -> bool:
            if not node:
                return True
            if node.val != val:
                return False
            return dfs(node.left, val) and dfs(node.right, val)

        if not root:
            return True
        return dfs(root, root.val)