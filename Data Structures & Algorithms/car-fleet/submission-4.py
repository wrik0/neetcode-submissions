class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        posSpeed = [(x, y) for x, y in zip(position, speed)]
        posSpeed.sort(reverse = True)
        for p, s in (posSpeed):
            stack.append((target - p)/s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

