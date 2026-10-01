class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 1

        for x in range(1, len(nums)):
            if candidate != nums[x]:
                if count == 0: 
                    candidate = nums[x]
                    count = 1
                else: count -= 1
            else:
                count += 1
        return candidate