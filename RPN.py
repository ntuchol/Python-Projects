def evaluate_rpn(expression):
    """
    Evaluate a Reverse Polish Notation (RPN) expression.
    :param expression: List of tokens in RPN (e.g., ["2", "1", "+", "3", "*"])
    :return: Result of the evaluation
    """
    stack = []
    operators = {"+", "-", "*", "/"}
    
    for token in expression:
        if token not in operators:
            # Push numbers onto the stack
            stack.append(float(token))
        else:
            # Pop the last two numbers for the operation
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


# Example usage
rpn_expression = ["2", "1", "+", "3", "*"]  # Equivalent to (2 + 1) * 3
result = evaluate_rpn(rpn_expression)
print(f"Result: {result}")  # Output: 9.0