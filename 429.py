# Problem link: https://leetcode.com/problems/n-ary-tree-level-order-traversal/

from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        ans = []   
        queue = deque()
        queue.append(root)
        
        while queue:
            newQueue = deque()
            currentLevel = []
            while queue:
                node = queue.popleft()
                currentLevel.append(node.val)
                for child in node.children:
                    newQueue.append(child)
            queue = newQueue
            ans.append(currentLevel)
        
        return ans