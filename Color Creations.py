from turtle import*
screen = Screen()
screen.setup(400, 400)
screen.bgcolor('white')
screen.bgcolor('#A7E30E')

colors = {
  'verylime': '#A7E30E',
  'reallyraspberry': '#FA057F'
}

print(colors['verylime'])
print(colors['reallyraspberry'])

screen.bgcolor(colors['verylime'])
color(colors['reallyraspberry'])
style = ('Arial', 40, 'bold')
write('HELLO', font=style, align = 'center')
hideturtle() 


