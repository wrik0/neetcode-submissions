class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count, i = 0, 0
        
        while i <= len(nums) -1 - count:
            if nums[i] != val: i += 1
            else: 
                nums[len(nums) -1 - count], nums[i] = nums[i], nums[len(nums) -1 - count]
                count += 1 

        return len(nums) - count