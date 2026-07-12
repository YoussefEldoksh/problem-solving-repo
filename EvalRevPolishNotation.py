
from collections import deque

def evalRPN(tokens) -> int:
    stack = deque()
    
    def isNumber(token):
        if token[0] == '-':
            if token[1:].isdigit():
                return True
        elif token[0] != '-':
            if token.isdigit():
                return True
        return False
    
    for token in tokens:
        print(stack)
        if isNumber(token):
            stack.append(int(token))
        else:
            operand1 = stack[-1]
            stack.pop()
  
            operand2 = stack[-1]
            stack.pop()
            
            if token == "+":
                stack.append(operand2 + operand1)
            elif token == "-":
                stack.append(operand2 - operand1)
            elif token == "*":
                stack.append(operand2 * operand1)
            elif token == "/":
                stack.append(int(operand2 / operand1))
    if len(stack) == 0:
        return None
    else:
        return stack[-1]
    
    
tokens = ["2","1","+","3","*"]

print(evalRPN(tokens))