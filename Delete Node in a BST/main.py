class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to be deleted found
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Find the in-order successor (smallest in the right subtree)
                successor = self.getMin(root.right)
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)

        return root

    def getMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
