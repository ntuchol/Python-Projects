def evaluate_prefix(expression):
    tokens = expression.split()
    stack = []
    for token in reversed(tokens):
        if token.isdigit():
            stack.append(int(token))
        else:
            if len(stack) < 2:
                raise ValueError("Invalid prefix expression")
            operand1 = stack.pop()
            operand2 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)
            else:
                raise ValueError("Invalid operator")
    if len(stack) != 1:
         raise ValueError("Invalid prefix expression")
    return stack.pop()