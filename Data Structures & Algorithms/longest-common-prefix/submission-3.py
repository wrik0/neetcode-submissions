class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = min(strs, key=len)

        for i, letter in enumerate(first):
            for s in strs:
                if s[i] != letter: 
                    return first[:i]

        return first