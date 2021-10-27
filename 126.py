# Problem link: https://leetcode.com/problems/word-ladder-ii/

from collections import deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        n = len(wordList)
        wordLength = len(beginWord)

        if endWord not in wordList:
            return []

        pathLength = {}
        previousWords = {}
        pathLength[beginWord] = 0
        for word in wordList:
            pathLength[word] = n + 5
            previousWords[word] = []

        queue = deque([(beginWord, 0)])

        while queue:
            current, dist = queue.popleft()
            prefix = ''
            for i in range(wordLength):
                for code in range(ord('a'), ord('z') + 1):
                    letter = chr(code)
                    newWord = prefix + letter + current[i + 1:]
                    newDist = dist + 1

                    if newWord in pathLength:
                        if newDist == pathLength[newWord]:
                            previousWords[newWord].append(current)
                        elif newDist < pathLength[newWord]:
                            previousWords[newWord] = [current]
                            pathLength[newWord] = newDist
                            queue.append((newWord, newDist))
                prefix += current[i]
        
        if not previousWords[endWord]:
            return []
        
        queue = deque([[endWord]])
        while True:
            path = queue.popleft()
            lastWord = path[-1]
            if lastWord == beginWord:
                queue.append(path)
                break
            for word in previousWords[lastWord]:
                queue.append(path + [word])

        for path in queue:
            path.reverse()

        return list(queue)