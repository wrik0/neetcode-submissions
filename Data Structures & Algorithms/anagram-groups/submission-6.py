class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_tally = [[0] * 26 for _ in strs]

        anagram_dict = defaultdict(list)
        for i, s in enumerate(strs):
            for j, c in enumerate(s):
                char_tally[i][ord(c) - ord("a")] += 1 
            anagram_dict[tuple(char_tally[i])].append(strs[i])


        return list(anagram_dict.values())