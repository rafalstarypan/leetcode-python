# Problem link: https://leetcode.com/problems/push-dominoes/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        
        # keep indexes of the first occurence of the letter to the right
        suffL = [n] * (n + 1)
        suffR = [n] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            suffL[i] = suffL[i + 1]
            suffR[i] = suffR[i + 1]
            if dominoes[i] == 'L':
                suffL[i] = i
            elif dominoes[i] == 'R':
                suffR[i] = i
        
        # keep indexes of the first occurence of the letter to the left during the iteration
        lastL = -1
        lastR = -1
        result = list(dominoes)
        
        for i in range(n):
            if dominoes[i] == 'L':
                lastL = i
                continue
            if dominoes[i] == 'R':
                lastR = i
                continue
                
            # check if current domino is moved to the right
            if lastR > lastL and (suffR[i] <= suffL[i] or i - lastR < suffL[i] - i):
                result[i] = 'R'
                
            # check if current domino is moved to the left
            if suffL[i] < suffR[i] and (lastL >= lastR or i - lastR > suffL[i] - i) :
                result[i] = 'L'
        
        return ''.join(result)