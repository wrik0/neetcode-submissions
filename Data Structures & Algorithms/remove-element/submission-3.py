class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        
        while i < n:
            if nums[i] != val: i += 1
            else: 
                n -= 1
                nums[n], nums[i] = nums[i], nums[n]

        return n