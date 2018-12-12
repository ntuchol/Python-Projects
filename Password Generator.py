import random 
chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
length = input('password length?')
length = int(length)

for p in range(3):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)