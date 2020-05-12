import turtle

# Draw Yertle's pond.
pond = turtle.Screen()
pond.setup(600, 400)
pond.bgcolor('light blue')
pond.title("Yertle's Pond")

# Draw Yertle's mud island.
mud = turtle.Turtle('circle')
mud.shapesize(stretch_wid=5, stretch_len=5, outline=None)
mud.pencolor('tan')
mud.fillcolor('tan')

# Draw a floating log.
SIDE = 80
ANGLE = 90
log = turtle.Turtle()
log.hideturtle()
log.pencolor('peru')
log.fillcolor('peru')
log.speed(0)
log.penup()
log.setpos(215, -30)
log.lt(45)
log.begin_fill()
for _ in range(2):
    log.fd(SIDE)
    log.lt(ANGLE)
    log.fd(SIDE / 4)
    log.lt(ANGLE)
log.end_fill()

# Put a knothole in the log.
knot = turtle.Turtle()
knot.hideturtle()
knot.speed(0)
knot.penup()
knot.setpos(245, 5)
knot.begin_fill()
knot.circle(5)
knot.end_fill()

# Draw Yertle the Turtle.
yertle = turtle.Turtle('turtle')
yertle.color('green')
yertle.speed(1)  # Slowest.
yertle.fd(200)
yertle.lt(180)
yertle.fd(200)
yertle.rt(176)
yertle.fd(205)
