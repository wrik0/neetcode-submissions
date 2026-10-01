class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        monoStack = []
        for pos, temp in enumerate(temperatures):
            while len(monoStack) != 0 and monoStack[-1][0] < temp: 
                tComp, posComp = monoStack.pop()
                res[posComp] = pos - posComp
            monoStack.append([temp, pos])
        return res 