# Problem link: https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        # remove zeros from the input
        nums = [x for x in nums if x > 0]
        n = len(nums)
        
        # no triangle can be formed
        if n < 3:
            return 0
        
        # triangle can't be formed if the following condition holds:
        # a + b <= c; where c is the longest side
        
        # number of all possible triplets
        triplets = n * (n - 1) * (n - 2)
        triplets //= 6
        
        # precalculate all possible sums of two sides
        pairs = []
        for i in range(n):
            for j in range(i + 1, n): 
                pairs.append(nums[i] + nums[j])
        
        nums.sort()
        pairs.sort()
        # index of the first pair that is big enough to form a triangle with the current element
        smallPair = 0
        
        # iterate over the longest side of the triangle
        for i in range(2, n):
            # find the next smallPair
            while smallPair < len(pairs) and pairs[smallPair] <= nums[i]:
                smallPair += 1
                
            # remove incorrect triplets from the answer
            if smallPair > 0:
                triplets -= smallPair
        
        return triplets