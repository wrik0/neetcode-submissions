class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = dict()
        for s in strs:
            h = self.alphabetHash(s)
            if h not in r.keys():
                r[h] = []
            r[h].append(s)
        return list(r.values())
        
    def alphabetHash(self, s: str) -> Tuple:
        alphaHash = [0] * 26
        for c in s:
            alphaHash[ord(c) - ord('a')] += 1
        return tuple(alphaHash)
