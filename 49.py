# Problem link: https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        
        for s in strs:
            sortedString = ''.join(sorted(s))
            if sortedString not in anagrams:
                anagrams[sortedString] = []
            anagrams[sortedString].append(s)
        
        return list(anagrams.values())