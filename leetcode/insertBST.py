from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        traverse = root
        node = TreeNode(val=val)
        while traverse:
            if val >traverse.val:
                if not traverse.right:
                    traverse.right = node
                    break
                traverse= traverse.right
            else:
                if not traverse.left:
                    traverse.left = node
                    break
                traverse = traverse.left
        return root if root else node