# turtle is a 2d graphics module
from turtle import *
import math
import random
# Variables
cursor_x = -340
cursor_y = 100
penup()
goto(cursor_x, cursor_y)
pendown()
# size of characters (character size)
cs = 80
#stops refreshing screen
tracer(0, 0)

# region Tree and snowflake functions
# recursive function that calls itself
def tree(size, levels, angle):
    if levels == 0:
        color("green")
        dot(size*0.5)
        color("black")
        return
    forward(size)
    right(angle)
    # Draws entire right subtree
    tree(size * 0.8, levels - 1, angle)
    left(angle * 2)
    # draws entire left subtree)
    tree(size * 0.8, levels - 1, angle)
    right(angle)
    # return to original position
    backward(size)

# Function creates a side of a snowflake
def snowflake_side(length, levels):
    if levels == 0:
        forward(length)
        return

    length /= 3.0
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)
    right(120)
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)

# Function creates a snowflake by calling the snowflake_side multiple times
#Hashed out the multi coloured sides code
def create_snowflake(sides, length):
    #colors = ["green", "blue", "purple", "black", "magenta"]
    for i in range(sides):
        #color(colors[i])
        snowflake_side(length, sides)
        right(360 / sides)
# endregion

# region Character functions - every function should end with the right turtle facing right
def H(size):
    left(90)
    forward(size)
    backward(size/2)
    right(90)
    forward(size/2)
    left(90)
    forward(size/2)
    backward(size)
    right(90)
def S(size):
    forward(size/2)
    left(90)
    forward(size/2)
    left(90)
    forward(size/2)
    right(90)
    forward(size/2)
    right(90)
    forward(size/2)
def M_tree(size):
    angle_depth = 155
    left(90)
    forward(size)
    right(angle_depth)
    forward((size*0.25)/(math.sin(math.radians(angle_depth))))
    left((angle_depth-90)*2)
    forward((size*0.25)/(math.sin(math.radians(angle_depth))))
    right(angle_depth)
    forward(size)

    left(180)
    forward(size)
    tree(35, 6, 30)
    right(90)
def M(size):
    angle_depth = 155
    left(90)
    forward(size)
    right(angle_depth)
    forward((size*0.25)/(math.sin(math.radians(angle_depth))))
    left((angle_depth-90)*2)
    forward((size*0.25)/(math.sin(math.radians(angle_depth))))
    right(angle_depth)
    forward(size)
    left(90)
def E(size):
    forward(size/2)
    backward(size/2)
    left(90)
    forward(size)
    right(90)
    forward(size/2)
    backward(size/2)
    right(90)
    forward(size/2)
    left(90)
    forward(size/2)
def I(size):
    forward(size/2)
    backward(size/4)
    left(90)
    forward(size)
    left(90)
    forward(size/4)
    left(180)
    forward(size/2)
def T(size):
    penup()
    forward(size/4)
    pendown()
    left(90)
    forward(size)
    left(90)
    forward(size/4)
    left(180)
    forward(size/2)
def Y(size):
    angle_depth = 40
    # Move to top left
    penup()
    left(90)
    forward(size)
    pendown()
    right(180-angle_depth)
    forward((size*0.25)/math.sin(math.radians(angle_depth)))
    left((90-angle_depth)*2)
    forward((size*0.25)/math.sin(math.radians(angle_depth)))
    right(180)
    forward((size*0.25)/math.sin(math.radians(angle_depth)))
    left(angle_depth)
    forward(size-((size*0.25)/math.tan(math.radians(angle_depth))))
    left(90)
def A(size):
    angle = math.degrees(math.atan(4))
    left(angle)
    forward(size/(math.sin(math.atan(4))))
    right((2*angle))
    right((180-math.atan(math.radians(4)))*2)
    forward(size/(math.sin(math.atan(4))))
    backward(size/(2*(math.sin(math.atan(4)))))
    right(180-angle)
    forward(size/4)
    right(180)
def C(size):
    dis_ratio = 0.129
    penup()
    forward(size/2)
    pendown()
    right(180)
    for x in range(0, 12):
        forward(size*dis_ratio)
        right(15)
    forward(size*dis_ratio)
def R(size):
    dis_ratio = 0.067
    left(90)
    forward(size)
    right(90)
    forward(size*0.23)
    #right(180)
    for x in range(0, 12):
        forward(size*dis_ratio)
        right(15)
    forward(size*dis_ratio)
    forward(size*0.23)
    right(180)
    forward(size*0.26)
    right(65)
    forward(size*0.55)
    left(65)
def U(size):
    dis_ratio = 0.067
    penup()
    left(90)
    forward(size)
    right(180)
    pendown()
    forward(size *0.712)
    for x in range(0, 12):
        forward(size*dis_ratio)
        left(15)
    forward(size*dis_ratio)
    forward(size *0.712)
    right(90)
def D(size):
    dis_ratio = 0.129
    left(90)
    forward(size)
    right(90)
    #forward(size*0.05)
    for x in range(0, 12):
        forward(size*dis_ratio)
        right(15)
    forward(size*dis_ratio)
    #forward(size*0.05)
    right(180)
#endregion

#region Move cursor
#Move to next character along
def n_along():
    global cursor_x
    global cursor_y
    cursor_x = cursor_x + cs * 0.7
    penup()
    goto(cursor_x, cursor_y)
    pendown()

#Move to next line down
def n_down():
    global cursor_x
    global cursor_y
    cursor_x = -360
    cursor_y = cursor_y - cs *1.2
    penup()
    goto(cursor_x, cursor_y)
    pendown()
#endregion

#region Function calls
#region MERRY
M_tree(cs)
n_along()
color("green")
E(cs)
color("red")
n_along()
R(cs)
color("blue")
n_along()
R(cs)
color("magenta")
n_along()
Y(cs)
color("purple")
n_down()
#endregion
#region CHRISTMAS
C(cs)
color("blue")
n_along()
H(cs)
color("red")
n_along()
R(cs)
color("#419f6a")
n_along()
I(cs)
color("#3c79b8")
n_along()
S(cs)
color("gold")
n_along()
T(cs)
color("tomato")
n_along()
M_tree(cs)
color("green")
n_along()
A(cs)
color("green")
n_along()
S(cs)
color("green")
n_down()
#endregion
#region DR
D(cs)
color("magenta")
n_along()
R(cs)
color("blue")
n_down()
#endregion
#region MUMA
M(cs)
color("black")
n_along()
U(cs)
color("turquoise")
n_along()
M(cs)
color("blue")
n_along()
A(cs)
n_along()
#endregion
#region Snowflakes
penup()
goto(150, -80)
color("blue")
pendown()
create_snowflake(5, 130)

penup()
goto(200, 250)
color("green")
pendown()
create_snowflake(3, 80)

penup()
goto(-50, -130)
color("turquoise")
pendown()
create_snowflake(3, 50)

penup()
goto(-10, -250)
color("black")
pendown()
create_snowflake(3, 55)

penup()
goto(-300, -250)
color("green")
pendown()
create_snowflake(3, 70)

penup()
goto(900, -150)
color("purple")
pendown()
create_snowflake(3, 20)

#creates multiple small silver snowflakes
for x in range(0,100):
    penup()
    goto(random.randint(-380,380),random.randint(-350,350))
    color("silver")
    pendown()
    create_snowflake(3, 10)
#endregion
#endregion

update()
penup()
goto(0,0)
pendown()
mainloop()