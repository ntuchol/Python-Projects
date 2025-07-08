

def infix_to_postfix(expression):
  """Converts an infix expression to postfix."""
  # Implementation of Shunting Yard Algorithm
  pass

def evaluate_postfix(postfix_expression):
  """Evaluates a postfix expression."""
  # Implementation of postfix evaluation
  pass

def evaluate_infix(infix_expression):
  """Evaluates an infix expression."""
  postfix = infix_to_postfix(infix_expression)
  result = evaluate_postfix(postfix)
  return result

# Example
expression = "2 + 3 * (4 - 1)"
result = evaluate_infix(expression)
print(f"Result of {expression}: {result}")