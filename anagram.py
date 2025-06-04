def are_anagrams_sorting(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return sorted(s1) == sorted(s2)

print(are_anagrams_sorting("listen", "silent")) # Output: True
print(are_anagrams_sorting("hello", "world")) # Output: False