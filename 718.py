# Problem link: https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        
        # dp solution: dp[j] - length of the longest common subarray
        # after processing 'i' elements from the first list and 'j' from the second
        dp = [0] * m
        ans = 0
        
        for i in range(n):
            newDp = [0] * m
            for j in range(m):
                # current elements are equal so try to make the common subarray longer
                if nums1[i] == nums2[j]:
                    if j != 0:
                        newDp[j] = dp[j-1] + 1
                    else:
                        newDp[j] = 1
                ans = max(ans, newDp[j])
            dp = newDp
        
        return ans