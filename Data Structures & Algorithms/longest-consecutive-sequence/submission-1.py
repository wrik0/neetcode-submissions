class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        arr = sorted(nums)
        tally = defaultdict(int)
        length = 1
        for el in arr:
            if el in tally:
                continue
            if (el - 1) in tally:
                tally[el] = tally.get(el - 1) + 1
                length = max(tally[el], length)
            else:
                tally[el] = 1

        return length
