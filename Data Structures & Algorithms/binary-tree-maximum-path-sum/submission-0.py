# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        s = root.val

        def maxNodeArm(node):
            nonlocal s
            if not node:
                return 0
            leftsum = max(0, maxNodeArm(node.left))
            rightsum = max(0, maxNodeArm(node.right))
            s = max(s, node.val + leftsum + rightsum)
            return node.val + max(leftsum, rightsum)

        _ = maxNodeArm(root)

        return s
