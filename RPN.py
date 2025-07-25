def evaluate_rpn(expression):
    
    stack = []
    operators = {"+", "-", "*", "/"}
    
    for token in expression:
        if token not in operators:
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b)
    
    return stack[0] if stack else None


rpn_expression = ["2", "1", "+", "3", "*"]  
result = evaluate_rpn(rpn_expression)
print(f"Result: {result}")  # Output: 9.0
