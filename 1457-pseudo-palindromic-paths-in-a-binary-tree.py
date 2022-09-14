"""
return number of path-to-leaf is a pseudo palindome
"""
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        count = [0]*10
        def traverse(node):
            nonlocal res
            if not node:
                return
            if not node.left and not node.right:
                # 遇到叶子结点，判断是否为伪回文串
                # 伪回文串路径上出现奇数次的数字个数不能大于 1
                count[node.val] += 1
                odd = 0
                for i in range(10):
                    if count[i] % 2:
                        odd += 1
                if odd <= 1:
                    res += 1
                # 返回上一步
                count[node.val] -= 1
                return
            count[node.val] += 1
            if node.left: traverse(node.left)
            if node.right: traverse(node.right)
            # 返回上一步
            count[node.val] -= 1
        traverse(root)
        return res
                
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        
        stack = [(root, 0)]
        while stack:
            node, path = stack.pop()
            if node is not None:
                # compute occurences of each digit
                # The idea is to keep the frequency of digit 1 in the first bit, 2 in the second bit, etc
                # move 1 to the left node.val times
                # 1^0 = 1, 1^1 = 0, occur even times will lead to 0 since 0^1^1=0
                path = path ^ (1 << node.val)
                if not node.left and not node.right:
                    # check if at most one digit has an odd frequency
                    # path-1 remove right most 1 from path
                    if path & (path-1) == 0:
                        res += 1
                else:
                    stack.append((node.right, path)) # path only include parent, will not change after node.left is visited
                    stack.append((node.left, path)) # path only include parent
        return res

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        
        def preorder(node, path):
            nonlocal res
            if node is not None:
                # compute occurences of each digit
                path = path ^ (1 << node.val)
                if not node.left and not node.right:
                    # check if at most one digit has an odd frequency
                    if path & (path-1) == 0:
                        res += 1
                else:
                    preorder(node.left, path)
                    preorder(node.right, path)
        preorder(root, 0)
        return res

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        
        cnt = [0]*10
        stack = [(root, cnt)]
        while stack:
            node, cnt = stack.pop()
            if node is not None:
                # compute occurences of each digit
                cnt[node.val] += 1
                if not node.left and not node.right:
                    # check if at most one digit has an odd frequency
                    odd = 0
                    for i in range(10):
                        if cnt[i] % 2:
                            odd += 1
                    if odd <= 1:
                        res += 1
                else:
                    stack.append((node.right, cnt[:])) # cnt is a reference and will change each call, make a deep copy
                    stack.append((node.left, cnt[:])) 
        return res





            
                