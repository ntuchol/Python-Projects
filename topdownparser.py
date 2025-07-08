import time
import random

class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.non_terminals = set(key for key in grammar)
        self.terminals = set()
        for productions in grammar.values():
            for production in productions:
                for symbol in production:
                    if symbol not in self.non_terminals:
                        self.terminals.add(symbol)

    def parse(self, input_string):
        stack = ["S"]
        input_list = list(input_string)
        
        while stack:
            top = stack[-1]
            current_input = input_list[0] if input_list else None

            if top in self.terminals or top == "$":
                if top == current_input:
                    stack.pop()
                    if input_list:
                        input_list.pop(0)
                else:
                    return False
            elif top in self.non_terminals:
                productions = self.grammar[top]
                found = False
                for production in productions:
                    if not production:
                        continue
                    if production[0] == current_input or production[0] in self.non_terminals or (current_input is None and production[0] == "$"):
                        stack.pop()
                        for symbol in reversed(production):
                            if symbol != "$":
                                stack.append(symbol)
                        found = True
                        break
                if not found:
                    return False
            else:
                return False
        return True if not input_list else False

def generate_random_input(length, terminals):
    return "".join(random.choice(list(terminals)) for _ in range(length))

def measure_parsing_time(parser, input_string, num_trials=10):
    start_time = time.time()
    for _ in range(num_trials):
        parser.parse(input_string)
    end_time = time.time()
    return (end_time - start_time) / num_trials

if __name__ == "__main__":
    grammar = {
    "S": [["A", "B"]],
    "A": [["a"], [""]],
    "B": [["b"], [""]]
    }

    parser = Parser(grammar)
    
    terminals = parser.terminals
    
    input_lengths = [5, 10, 20, 30, 40, 50]
    
    for length in input_lengths:
        input_string = generate_random_input(length, terminals)
        parsing_time = measure_parsing_time(parser, input_string)
        print(f"Input Length: {length}, Parsing Time: {parsing_time:.6f} seconds")