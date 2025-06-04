 lookaheads for more complex patterns:


import re

# Match 'foo' only if it is followed by 'bar' and NOT followed by 'baz'
pattern = r'foo(?=bar)(?!baz)'
text = "foobar foobaz foobarqux"

matches = re.findall(pattern, text)
print(matches)  # Output: ['foo']