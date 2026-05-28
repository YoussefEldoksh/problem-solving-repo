
class Solution:
    def isBalanced(self, root) -> bool:
        def hight():
            if not root:
                return [True,0]
            left = hight(root.left) 
            right = hight(root.right) 
            balanced = (right[0] and left[0] and abs(left[1]-right[1]) <= 1)
            return [balanced , 1 + max(left[1],right[1])]
        
        hightOfTree = hight()

        return hightOfTree[0]

        
