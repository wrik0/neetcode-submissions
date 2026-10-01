from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = defaultdict(int)

        for num in nums:
            if hashMap[num] > 0: return True
            hashMap[num] += 1

        return False
