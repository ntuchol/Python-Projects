import re

pattern = r'foo(?=bar)(?!baz)'
text = "foobar foobaz foobarqux"

matches = re.findall(pattern, text)
print(matches)  
