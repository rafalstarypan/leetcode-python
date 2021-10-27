# Problem link: https://leetcode.com/problems/map-sum-pairs/

class MapSum:

    def __init__(self):
        self.wordValue = dict()
        self.prefixSum = dict()
        

    def insert(self, key: str, val: int) -> None:
        toAdd = val
        if key in self.wordValue:
            toAdd = val - self.wordValue[key]
        self.wordValue[key] = val
            
        prefix = ''
        for letter in key:
            prefix += letter
            if prefix not in self.prefixSum:
                self.prefixSum[prefix] = 0
            self.prefixSum[prefix] += toAdd
            

    def sum(self, prefix: str) -> int:
        if prefix not in self.prefixSum:
            return 0
        return self.prefixSum[prefix]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)