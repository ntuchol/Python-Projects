def print_name(name):
  print(name)

print_name("World") 
print_name("Python") 

def check_case(text):
    if text.isupper():
        print("The string is in uppercase.")
    elif text.islower():
        print("The string is in lowercase.")
    else:
        print("The string is mixed case or contains non-alphabetic characters.")

check_case("HELLO")
check_case("world")
check_case("MixEdCase")
check_case("123")

import sys

if __name__ == "__main__":
    print("Command-line arguments:")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")

import click
    
    @click.command()
    @click.option('--name', default='World', help='The person to greet.')
    @click.option('--times', default=1, help='Number of greetings.')
    def greet(name, times):
        for _ in range(times):
            click.echo(f"Hello, {name}!")
    
    if __name__ == '__main__':
        greet()

   import fire
    
    class MyClass:
        def method1(self, arg1, arg2):
            return f"Method 1 called with {arg1} and {arg2}"
    
        def method2(self):
             return "Method 2 called"
    
    if __name__ == '__main__':
        fire.Fire(MyClass)

names = ['smogtether', 'two']
print([n[0].upper() for n in names])
def alternate_even_odd(start=0):
    
    num = start
    while True:
        yield num
        num += 1
        yield num
        num += 1
