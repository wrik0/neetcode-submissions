class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pdtAr = [1] * len(nums)
        pdt = 1
        for i in range(len(nums)):
            pdtAr[i] *= pdt 
            pdt *= nums[i]

        pdt = 1
        for i in range(len(nums) -1, -1, -1):
            pdtAr[i] *= pdt
            pdt *= nums[i]
        
        return pdtAr
    