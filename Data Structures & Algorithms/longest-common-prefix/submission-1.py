class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min([len(s) for s in strs])
        res = ""

        for i in range(min_length):
            for s in strs:
                if s[i] == strs[0][i]: 
                    continue
                else:
                    return res
            res += strs[0][i]

        return res