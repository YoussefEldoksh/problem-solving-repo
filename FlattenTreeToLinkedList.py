# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        arr = []

        def preOrder(root):
            if not root:
                return 
            arr.append(root)
            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)
        for i in range(len(arr) - 1):
            arr[i].left = None
            arr[i].right = arr[i + 1]

        