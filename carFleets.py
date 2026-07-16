from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = deque()
        n = len(position)
        fleets = 0
        combined = sorted(zip(position, speed), key=lambda x: -x[0])
        print(combined)

        for i in range(0,n):
            stack.append((target - combined[i][0])/combined[i][1])
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()


        return len(stack)