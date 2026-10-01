class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        numMap = {}

        for v in reversed(nums2):
            while stack and stack[-1] <= v:
                stack.pop()
            numMap[v] = stack[-1] if stack else -1
            stack.append(v)
        
        return [numMap[i] for i in nums1]
