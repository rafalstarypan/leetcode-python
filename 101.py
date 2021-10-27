# Problem link: https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isPalindrome(self, nodes: List[TreeNode]) -> bool:
        l = 0
        r = len(nodes) - 1
        while l < r:
            if nodes[l] and nodes[r] and nodes[l].val != nodes[r].val:
                return False
            if (nodes[l] and not nodes[r]) or (not nodes[l] and nodes[r]):
                return False
            l += 1
            r -= 1
            
        return True
        
    def isSymmetric(self, root: TreeNode) -> bool:
        treeLevel = [root]
        
        while treeLevel:
            if not self.isPalindrome(treeLevel):
                return False
            
            newTreeLevel = []
            for node in treeLevel:
                if node:
                    newTreeLevel.append(node.left)
                    newTreeLevel.append(node.right)
            treeLevel = newTreeLevel
        
        return True