"""

Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

The inorder successor of a particular node is simply the node that comes after this node during the inorder traversal of the tree.

solution 1. brute force inorder

solution 2. We define two class variables for this algorithm: previous and inorderSuccessorNode. The previous variable will only be used when handling the second case as previously explained and the inorderSuccessorNode will ultimately contain the result to be returned.
we first check which of the two cases we need to handle. For that, we simply check for the presence of a right child.
a. The right child exists
-> find the leftmost node
b. The right child does not exist
-> For this, we define another function called inorderCase2 and we will pass it a node and the node p.
-> We perform simple inorder traversal and hence, we first recurse on the left child of the node.
-> Then, when the recursion returns, we check if the class variable previous is equal to the node p. If that is the case, then it means p is the inorder predecessor of node or in other words, the node is the inorder successor of the node p and we return from that point onwards. We assign inorderSuccessorNode to node and return from this function.

solution 3. By comparing the values of the node p and the current node in the tree during our traversal, we can discard half of the remaining nodes at each step, and thus, for a balanced binary search tree we can search for our inorder successor in logarithmic time rather than linear time.

--> We start our traversal with the root node and continue the traversal until our current node reaches a null value
--> At each step we compare the value of node p with that of node:
	if p.val >= node.val: discard the left subtree and update node = node.right
	if p.val < node.val: that implies that the successor must lie in the left subtree and that the current node is a potential candidate for inorder successor. move towards left subtree
	REPEAT the comparison until None
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# brute force inorder
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root] + inorder(root.right)
        
        tree = inorder(root)
        
        for i in range(len(tree)-1):
            if tree[i].val == p.val:
                return tree[i+1]
        return None

class Solution:
	# optimized inorder Time: O(N) - worst, O(nlogn) - average
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        self.previous = None
        self.inorder_successor_node = None
        
        # case 1: find the leftmost node in the right subtree if p has right subtree
        if p.right:
            leftmost = p.right
            while leftmost.left:
                leftmost = leftmost.left
            self.inorder_successor_node = leftmost
        # case 2: perform the standard inorder traversal and keep track of the previous node
        else:
            self.inordercase2(root, p)
            
        return self.inorder_successor_node
    

    def inordercase2(self, node: TreeNode, p: TreeNode):
        if not node:
            return
        # recurse on the left side
        self.inordercase2(node.left, p)
        
        # check if previous is the inorder predecessor of node
        if self.previous == p and not self.inorder_successor_node:
            self.inorder_successor_node = node
            return
        
        # update previous
        self.previous = node
        
        self.inordercase2(node.right, p)
        
class Solution:
	# Time: O(N) - worst, O(nlogn) - average
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
                
        return successor

