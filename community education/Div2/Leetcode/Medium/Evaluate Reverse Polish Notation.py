class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in range(len(tokens)):
            x = tokens[n]
            if x == "+":
                stack[-2] += stack[-1]
                stack.pop()
            elif x == "-":
                stack[-2] -= stack[-1]
                stack.pop()
            elif x == "*":
                stack[-2] *= stack[-1]
                stack.pop()
            elif x == "/":
                stack[-2] = int(stack[-2] / stack[-1])
                stack.pop()
            else:
                stack.append(int(x))
        return stack[0]