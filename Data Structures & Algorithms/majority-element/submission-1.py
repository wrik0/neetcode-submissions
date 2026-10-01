class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0

        for x in range(len(nums)):
            if count == 0: 
                candidate = nums[x]
            count += 1 if candidate == nums[x] else -1
        return candidate