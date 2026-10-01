class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(self.operate(a, b, token))
        return stack[-1]

    def operate(self, a: int, b: int, operator: char) -> int:
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "/":
            return int(a / b)
        else:
            return a * b