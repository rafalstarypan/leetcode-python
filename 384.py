# Problem link: https://leetcode.com/problems/shuffle-an-array/

from random import choice

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original
    

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.original)
        indexes = list(range(0, n))
        
        shuffled = []
        for i in range(n):
            chosenPos = choice(indexes)
            shuffled.append(self.original[chosenPos])
            indexes.remove(chosenPos)
            
        return shuffled
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()