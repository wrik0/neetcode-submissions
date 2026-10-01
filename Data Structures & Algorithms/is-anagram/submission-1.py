class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.getAnagramHash(s) == self.getAnagramHash(t)

    def getAnagramHash(self, s: str) -> Tuple:
        alphabetMap = [0] * 26
        for char in s:
            alphabetMap[ord(char) - ord('a')] += 1
        return tuple(alphabetMap)