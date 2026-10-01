class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_tally = [[0] * 26 for _ in strs]

        for i, s in enumerate(strs):
            for j, c in enumerate(s):
                char_tally[i][ord(c) - ord("a")] += 1 

        anagram_dict = defaultdict(list)

        for string_idx, signature in enumerate(char_tally):
            anagram_dict[tuple(signature)].append(strs[string_idx])

        return list(anagram_dict.values())