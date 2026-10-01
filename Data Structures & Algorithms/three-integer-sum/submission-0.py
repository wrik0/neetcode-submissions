class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        res = []
        l = 0
        for i, a in enumerate(arr):
            if i > 0 and a == arr[i - 1]:
                continue
            
            l, r = i + 1, len(arr) - 1
            while l < r:
                threeSum = a + arr[l] + arr[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, arr[l], arr[r]])
                    l += 1
                    while arr[l] == arr[l - 1] and l < r:
                        l += 1
        return res