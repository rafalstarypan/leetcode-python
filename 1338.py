# Problem link: https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # length of the array
        n = len(arr)
        
        # count occurences of every number
        cnt = dict()
        for x in arr:
            if x not in cnt:
                cnt[x] = 0
            cnt[x] += 1
        
        occurences = list(cnt.values())
        occurences.sort(reverse = True)
        
        removedSoFar = 0
        ans = 0
        
        # remove the number with maximal number of occurences
        # and check the condition
        for x in occurences:
            removedSoFar += x
            ans += 1
            if removedSoFar >= n//2:
                break
        
        return ans