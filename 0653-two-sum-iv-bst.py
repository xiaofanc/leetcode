import collections

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
    def findTarget(self, root, k) :
        def tranversal(root):
            if not root:
                return []
            return tranversal(root.left) + [root.val] + tranversal(root.right)
        tree = tranversal(root)
        (tree)
        for i in range(len(tree)):
            for j in range(i+1, len(tree)):
                if tree[i]+tree[j] == k:
                    return True
        return False

    # two pointers
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = self.inorder(root)
        lo, hi = 0, len(nums)-1
        while lo < hi:
            s = nums[lo] + nums[hi]
            if s == k:
                return True
            elif s < k:
                lo += 1
            else:
                hi -= 1               
        return False
          
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def findTarget(self, root, k) :
        def tranversal(root):
            if not root:
                return []
            return tranversal(root.left) + [root.val] + tranversal(root.right)
        tree = tranversal(root)
        l, r = 0, len(tree)-1
        while l < r:
            if tree[l]+tree[r] == k:
                return True
            elif tree[l]+tree[r] > k:
                r -= 1
            else:
                l += 1
        return False
            
    # hashset
    def findTarget(self, root, k) :
        seen = []
        def find(root, k, seen):
            if not root:
                return False
            if k - root.val in seen:
                return True
            seen.append(root.val)
            return find(root.left, k, seen) or find(root.right, k, seen)
        return find(root, k, seen)

    
    # bfs + hashset
    def findTarget(self, root, k):
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False


    # import queue
    def findTarget(self, root, k):
        if not root:
            return False
        s = set()
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            complement = k - node.val
            if complement in s:
                return True
            else:
                s.add(node.val)
            if node.left:  q.put(node.left)
            if node.right: q.put(node.right)
        return False

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        
        visited = set()
        
        queue = collections.deque([root])
        
        while queue:
            for _ in range(len(queue)):
                node = queue.pop()
                if k - node.val in visited:
                    return True
                visited.add(node.val)
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
        
        return False


if __name__ == '__main__':
    T = TreeNode
    root = T(1, T(2), T(3,T(4)))
    s = Solution()
    print(s.findTarget(root, 4))

