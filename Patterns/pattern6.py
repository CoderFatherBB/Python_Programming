import turtle
a=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
col=('pink','red','yellow','blue')
a.speed(0)
for i in range(500):
	a.pencolor(col[i%4])
	a.setheading(i*95)
	for b in range(4):
		a.forward(i*1)
		a.right(300)