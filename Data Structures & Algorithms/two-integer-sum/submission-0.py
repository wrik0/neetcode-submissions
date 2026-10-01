class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tally = dict()

        for k, v in enumerate(nums):
            diff = target - v
            if diff in tally.keys():
                return [tally[diff], k]
            tally[v] = k