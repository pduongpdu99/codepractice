from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            rl = root.left
            rr = root.right
            root.left = rr
            root.right = rl
            
            if root.left:
                self.invertTree(root.left)
            
            if root.right:
                self.invertTree(root.right)
        return root
            
            