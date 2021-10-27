# Problem link: https://leetcode.com/problems/combination-sum/

class Solution:
    def findCombinations(self, curSum, chosen, target, candidates):
        if curSum > target:
            return []
        if curSum == target:
            return [chosen]
        
        res = []
        for cand in candidates:
            if chosen and cand < chosen[-1]:
                continue
            new_chosen = chosen + [cand]
            combinations = self.findCombinations(curSum + cand, new_chosen, target, candidates)
            if combinations:
                res += combinations
                
        return res
    
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.findCombinations(0, [], target, candidates)
        