class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: # stack[-1][0] <- Gets the temperature values from the top of stack
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = (index - stackIndex)
            stack.append([temp, index])
        return res