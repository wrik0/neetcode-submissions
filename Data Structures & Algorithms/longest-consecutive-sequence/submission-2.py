class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = sorted(nums)
        tally = defaultdict(int)
        length = 0
        for el in arr:
            if el in tally:
                continue
            if (el - 1) in tally:
                tally[el] = tally.get(el - 1) + 1
            else:
                tally[el] = 1
            length = max(tally[el], length)

        return length
