

def infix_to_postfix(expression):
  pass

def evaluate_postfix(postfix_expression):
  pass

def evaluate_infix(infix_expression):
  postfix = infix_to_postfix(infix_expression)
  result = evaluate_postfix(postfix)
  return result

expression = "2 + 3 * (4 - 1)"
result = evaluate_infix(expression)
print(f"Result of {expression}: {result}")
