class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            tally = [0] * 26
            for c in s:
                tally[ord(c) - ord('a')] += 1
            res[tuple(tally)].append(s)
        return res.values()