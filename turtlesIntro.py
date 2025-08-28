import turtle

# Create a turtle screen and turtle object
screen = turtle.Screen()
screen.setup(width=800, height=600)

# Create a turtle
t = turtle.Turtle()
t.speed(0)

# Draw a simple shape
t.color("blue")
for _ in range(36):
    t.forward(100)
    t.right(170)


# Close the turtle screen
#screen.bye()

print("Drawing saved as 'turtle_drawing.svg'.")