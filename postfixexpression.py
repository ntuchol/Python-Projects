import math

def evaluatePostfix(arr: list[str]) -> int:
    stack = []

    for token in arr:
        if token.lstrip('-').isdigit():  
            stack.append(int(token))
        else:
            val1 = stack.pop()
            val2 = stack.pop()

            if token == "+":
                stack.append(val2 + val1)
            elif token == "-":
                stack.append(val2 - val1)
            elif token == "*":
                stack.append(val2 * val1)
            elif token == "/":
                stack.append(math.trunc(val2 / val1))

    return stack.pop()

if __name__ == "__main__":
    arr = ["2", "3", "1", "*", "+", "9", "-"]
    print(evaluatePostfix(arr)) 
