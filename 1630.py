# Problem link: https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def isArithmetic(self, a: List[int]) -> bool:
        n = len(a)
        if n < 2:
            return False
        
        a.sort()
        diff = a[1] - a[0]
        
        for i in range(2, n):
            if a[i] - a[i-1] != diff:
                return False
        return True
        
        
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        ans = [-1] * n
        
        for i in range(n):
            sublist = nums[l[i] : r[i] + 1]
            ans[i] = self.isArithmetic(sublist)
        
        return ans