# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        
        if not root:
            return []
        total = []
        while queue:
            lenght = len(queue)
            res = []
            for i in range(len(queue)):
                node = queue.popleft()
                res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            total.append(res)
        return total
            