import turtle
obj=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor('black')
col=('red','yellow','green','cyan','blue','white')
obj.speed(0)
for i in range(120):
	obj.circle(i+8)
	obj.left(30)
	obj.color(col[i%6])
	
turtle.done()