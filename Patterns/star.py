import turtle
col = ('red','yellow','green','cyan','blue','white')

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(30)

for i in range (100):
	t.color(col[i%6])
	t.forward(i*4)
	t.left(150) #changing this creates different shape 
	t.width(4) #changing this creates different pattern in center