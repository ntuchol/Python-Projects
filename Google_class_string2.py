#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
s = 'joining'
def verbing(s):
    if s[-3:] == 'ing':
        s = s + 'ly'
    elif (s[-3:] != 'ing') & (len(s) >= 3):
        s = s + 'ing'
    return s
    
print(verbing(s))

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
s = 'This dinner is not that bad!'
def not_bad(s):
       instance_not = s.find('not')
       instance_bad = s.find('bad')
       if instance_bad > instance_not:
           s = s[:instance_not] + 'good' + s[instance_bad+3:]
       return s
print(not_bad(s)) 


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
a = 'abcde'
b = 'fghijk'
def front_back(a, b):
  a_middle = len(a) / 2
  b_middle = len(b) / 2
  if len(a) % 2 == 1:  
    a_middle = a_middle + 1
  if len(b) % 2 == 1:
    b_middle = b_middle + 1
    
    a_front = a[:a_middle]
    a_back = b[:b_middle]
    b_front = b[b_middle:]
    b_back = b[b_middle:]
    new_string = a_front + a_back + b_front + b_back
    return new_string

print(front_back(a,b))

