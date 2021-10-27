# Problem link: https://leetcode.com/problems/custom-sort-string/

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        letterPos = {}
        
        for index, letter in enumerate(order):
            letterPos[letter] = index
            
        for i in range(97, 123):
            if chr(i) not in letterPos:
                letterPos[chr(i)] = -1
        
        l = sorted(s, key=(lambda letter: letterPos[letter]))
        
        return ''.join(l)