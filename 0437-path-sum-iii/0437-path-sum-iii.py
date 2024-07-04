# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, current_sum):
            nonlocal count
            if not node:
                return

            current_sum += node.val

            count += prefix_sum_count.get(current_sum - targetSum, 0)

            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            prefix_sum_count[current_sum] -= 1

        count = 0
        prefix_sum_count = {0: 1}
        dfs(root, 0)
        return count