import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")

# Create a turtle named "drawer"
drawer = turtle.Turtle()
drawer.color("black")
drawer.pensize(2)

# Function to draw a rectangle
def draw_rectangle(width, height):
    for _ in range(2):
        drawer.forward(width)
        drawer.right(90)
        drawer.forward(height)
        drawer.right(90)

# Function to draw a triangle
def draw_triangle(size):
    for _ in range(3):
        drawer.forward(size)
        drawer.left(120)

# Function to draw a circle
def draw_circle(radius):
    drawer.circle(radius)

# Draw the tree trunk
drawer.penup()
drawer.goto(-15, -50)  # Position the turtle
drawer.pendown()
draw_rectangle(30, 100)

# Draw the foliage with triangles
drawer.penup()
drawer.goto(-50, 50)  # Position the turtle
drawer.pendown()
draw_triangle(100)

drawer.penup()
drawer.goto(-40, 100)  # Position the turtle
drawer.pendown()
draw_triangle(80)

drawer.penup()
drawer.goto(-30, 140)  # Position the turtle
drawer.pendown()
draw_triangle(60)

# Hide the turtle and display the window
drawer.hideturtle()
wn.mainloop()
