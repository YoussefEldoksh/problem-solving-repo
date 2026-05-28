class Solution:
    def maxDepth(self, root) -> int:

        def hight(root):
            if not root:
                return 0
            left,right = hight(root.left), hight(root.right)
            
            return 1 + max(left,right)
        hightOfTree = hight(root)
        return hightOfTree