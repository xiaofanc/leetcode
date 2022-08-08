# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # if delete a leaf node: return root
        # if delete a node without left subtree: return right subtree to the parent
        # if delete a node without right subtree: return left subtree to the parent
        # if delete a node with left and right subtree:
        # find the first node > key from the right subtree, swap them and delete
        # if node not found
        # print("root ->", root, key)
        if not root:
            return
        prev, cur = None, root
        while cur:
            prev = cur
            if key > cur.val:
                cur = cur.right
            elif key < cur.val:
                cur = cur.left
            else:
                if not cur.left and not cur.right:
                    return None
                elif not cur.left:
                    if prev.val > key:
                        prev.left = cur.right
                    else:
                        prev.right = cur.right
                elif not cur.right:
                    if prev.val > key:
                        prev.left = cur.left
                    else:
                        prev.right = cur.left
                else:
                    # find the first node > key from the right subtree
                    node = cur.right
                    while node.left:
                        node = node.left
                    # replace node with key
                    cur.val = node.val
                    # delete the node
                    cur.right = self.deleteNode(cur.right, cur.val)
        return root
                
                
                    
            