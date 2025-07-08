from pydraw import *

screen = Screen(800, 600, 'My First Project!')

box = Rectangle(screen, 50, 50, 50, 50) 

def mousedown(button, location):
  print(f'Wow, the {button}-button on the mouse!')

def mouseup(button, location):
  print('How un-impressive...')

def keydown(key):
  print(f'Keyboard input is {key} to creating interactive programs!')

def keyup(key):
  print('For when you really just gotta stop moving, keyup is here to save you.')

# All of the above methods must be defined above this statement (because Python):
screen.listen()


# -- As you can see, user input is as simple as defining methods and telling pydraw to listen!
#    This feature has been long overdue for teachers who want to teach Python to their students
#    by making really cool stuff but can't escape how ridiculously input has been handled in the past.
#    Now defining user input is easy to understand and use.

fps = 30
running = True
while running:
    screen.update()
    screen.sleep(1 / fps)

screen.exit()