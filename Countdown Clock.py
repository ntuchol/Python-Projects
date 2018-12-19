import time

time_ = int(input("Enter the number of seconds you want to count down from: "))

while time_ >= 0:
  print(time_)
  time.sleep(1)
  time_ -= 1

print("Time's up!")
