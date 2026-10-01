class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for idx, num in enumerate(nums):
            diff = target - num
            if num in d.keys():
                return [d.get(num), idx]
            d[diff] = idx
        return list()