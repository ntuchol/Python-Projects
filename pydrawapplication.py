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

screen.listen()

fps = 30
running = True
while running:
    screen.update()
    screen.sleep(1 / fps)

screen.exit()
