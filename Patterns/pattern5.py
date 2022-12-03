import turtle 
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
t.speed(0)
screen.setup(700, 700)
col=('yellow', 'red', 'cyan', 'purple')
for c in range(450):
	t.pencolor(col[c%4])
	t.width(2)
	t.forward(c)
	t.right(89)
	t.forward(c*2)
	t.right(89)