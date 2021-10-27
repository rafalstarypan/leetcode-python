# Problem link: https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        # first element is a peak
        if n == 1 or nums[0] > nums[1]:
            return 0
        
        # last element is a peak
        if nums[-1] > nums[-2]:
            return n - 1
        
        # binary search to find a peak
        lo = 1
        hi = n - 2
        while lo < hi:
            mid = (lo + hi) // 2
            # mid is a peak
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] > nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return lo