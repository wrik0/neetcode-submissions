class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        tally1 = defaultdict(int)
        for char in s:
            tally1[char] += 1
        
        tally2 = defaultdict(int)
        for char in t:
            tally2[char] += 1

        for k, v in tally1.items():
            if tally2[k] != v: return False
        
        return True