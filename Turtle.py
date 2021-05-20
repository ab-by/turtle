import turtle

#creating turtle pen
pen= turtle.Turtle()
window = turtle.Screen() #screen with canavas

#set the fillcolor
pen.fillcolor('yellow')

#starting the filling code
pen.begin_fill()

#drawing the circle of radius r
pen.up()
pen.goto(0,-120)
pen.circle(200)
 
 # ending the filling of the color
pen.end_fill()

#eye 1
pen.fillcolor('white')
pen.begin_fill()
pen.up()
pen.goto(-70,130)
pen.down()
pen.pensize(2)
pen.circle(40)
pen.end_fill()

# eyeball 1
pen.fillcolor('black')
pen.begin_fill()
pen.up()
pen.goto(-70,140)
pen.down()
pen.circle(20)
pen.end_fill()

#eye 2
pen.fillcolor('white')
pen.begin_fill()
pen.up()
pen.goto(70,130)
pen.down()
pen.pensize(2)
pen.circle(40)
pen.end_fill()

# eyeball 2
pen.fillcolor('black')
pen.begin_fill()
pen.up()
pen.goto(70,140)
pen.down()
pen.circle(20)
pen.end_fill()

#mouth
pen.up()
pen.goto(-100,20)
pen.down()
pen.pensize(4)
pen.right(90)
pen.circle(100,180)
pen.left(90)
pen.forward(200)



