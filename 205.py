# Problem link: https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        
        mapToT = {}     # for every letter in s keep the correspongind one in t 
        mapToS = {}     # for every letter in t keep the correspongind one in s
        
        for i in range(n):
            # character in s has already been assigned with a different character
            if s[i] in mapToT and t[i] != mapToT[s[i]]:
                return False
            
            # character in t has already been assigned with a different character
            if t[i] in mapToS and s[i] != mapToS[t[i]]:
                return False
            
            mapToT[s[i]] = t[i]
            mapToS[t[i]] = s[i]
        
        return True