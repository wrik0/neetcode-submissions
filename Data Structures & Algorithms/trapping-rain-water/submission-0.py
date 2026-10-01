class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxH = 0
        area = 0
        while l < r:
            print(f"height[{l}]: {height[l]} height[{r}]: {height[r]} h: {maxH}")
            h = min(height[l], height[r])
            maxH = max(maxH, h)
            if height[l] > height[r]: # right ptr moves
                print(f"right ptr moves: abs({maxH} - {height[r]})")
                area += max(maxH - height[r], 0)
                r -= 1
            elif height[l] <= height[r]: # left ptr moves
                print(f"left ptr moves: abs({maxH} - {height[l]})")
                area += max(maxH - height[l], 0)
                l += 1
        return area
