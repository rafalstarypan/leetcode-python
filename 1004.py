# Problem link: https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def checkLengthOfOnes(self, pref: List[int], cand: int, k: int) -> bool:
        n = len(pref)
        for i in range(n-cand+1):
            zeroCnt = pref[i + cand - 1]
            if i > 0:
                zeroCnt -= pref[i-1]
            if zeroCnt <= k:
                return True
        return False
        
    def longestOnes(self, nums: List[int], k: int) -> int:
        # binary search the answer
        # for every index check if it is possible to create a sequence starting there
        n = len(nums)
        lo = 0
        hi = n
        
        # prepare prefix array to get number of 0 in subarray in O(1) time
        pref = [1 if nums[0] == 0 else 0]
        for i in range(1, n):
            add = 0
            if nums[i] == 0:
                add = 1
            pref.append(pref[-1] + add)
        
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.checkLengthOfOnes(pref, mid, k):
                lo = mid
            else:
                hi = mid-1
        
        return lo