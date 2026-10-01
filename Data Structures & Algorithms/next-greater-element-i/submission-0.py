class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Map = { num: i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        mono = []
        for i in range(len(nums2)):
            el = nums2[i]
            while mono and el > mono[-1]:
                val = mono.pop()
                idx = nums1Map[val]
                res[idx] = el
            if el in nums1Map:
                mono.append(el)

        return res