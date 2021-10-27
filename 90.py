# Problem link: https://leetcode.com/problems/subsets-ii/

class Solution:
    def getSubset(self, mask: int) -> List[int]:
        res = []
        
        for i in range(self.n):
            if mask & (1 << i):
                res.append(self.nums[i])
        
        res.sort()
        return res
        
        
    def equalLists(self, a: List[int], b: List[int]) -> bool:
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
    
    
    def contains(self, subset: List[int]) -> bool:
        for l in self.ans:
            if self.equalLists(l, subset):
                return True
        return False
    
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.nums = nums
        self.ans = []
        
        for mask in range((1 << self.n)):
            subset = self.getSubset(mask)
            if not self.contains(subset):
                self.ans.append(subset)
        
        return self.ans