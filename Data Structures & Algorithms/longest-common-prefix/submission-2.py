class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min([len(s) for s in strs])
        res = ""

        for i in range(min_length):
            letter = strs[0][i]
            for s in strs:
                if s[i] != letter: 
                    return res
            res += letter

        return res