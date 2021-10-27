# Problem link: https://leetcode.com/problems/partition-array-into-disjoint-intervals/

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        
        # maximum value in the left subarray must be smaller or equal
        # to the minimum in the right subarray
        # minimum value at the suffix of the array starting at position i
        suffMin = [0] * n
        suffMin[n-1] = nums[n-1]
        
        for i in range(n-2, -1, -1):
            suffMin[i] = min(suffMin[i + 1], nums[i])
        
        # maximum in the left subarray
        leftMax = -1
        for i in range(n-1):
            leftMax = max(leftMax, nums[i])
            if leftMax <= suffMin[i + 1]:
                return i + 1
        
        # no valid partition found
        return -1