class MinStack:

    def __init__(self):
        self.__stack = []

    def push(self, val: int) -> None:
        if len(self.__stack) == 0:
            self.__stack.append([val, val])
        else: 
            prev_min = self.__stack[-1][-1]
            self.__stack.append([val, min(val, prev_min)]) 

    def pop(self) -> None:
        self.__stack.pop()

    def top(self) -> int:
        return self.__stack[-1][0]

    def getMin(self) -> int:
        return self.__stack[-1][-1]
