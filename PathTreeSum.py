# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def pathSum(root,pathsum=0):
            if not root:
                return False

            pathsum += root.val
            if not root.left and not root.right:
                return pathsum == targetSum

            return  (pathSum(root.left,pathsum)) or (pathSum(root.right,pathsum))
            

        return pathSum(root)
