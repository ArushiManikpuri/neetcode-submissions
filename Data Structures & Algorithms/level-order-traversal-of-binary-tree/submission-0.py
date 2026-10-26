# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        result = []
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                pop_ele = q.popleft()
                level.append(pop_ele.val)
                if pop_ele.left:
                    q.append(pop_ele.left)
                if pop_ele.right:
                    q.append(pop_ele.right)
            result.append(level)  
        return result          

        