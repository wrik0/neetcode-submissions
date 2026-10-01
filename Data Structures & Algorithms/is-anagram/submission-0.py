class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.mapsEqual(self.calculateMap(s), self.calculateMap(t))
        
    def calculateMap(self, s: str) -> dict:
        tally = dict()
        for x in range(len(s)):
            char = s[x]
            tally[char] = tally.get(char, 0) + 1
        return tally
    

    def mapsEqual(self, a: dict, b: dict) -> bool:
        if len(a.keys()) != len(b.keys()):
            return False
        for key in a:
            if a[key] != b.get(key, 0):
                return False
        return True