from turtle import *
import random
import math
import Variables_Mandelbrot
from Cursor import n_along, n_down

# region Character functions - every function should end with the right turtle facing right
fibsequence = [0.5, 0.5, 1, 1, 1.5, 1.5, 2.5, 2.5, 4, 4, 6.5, 6.5, 10.5, 10.5, 18.5, 18.5]
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
def B(size):
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
    forward(size*0.23)
    for x in range(0, 12):
        forward(size*dis_ratio)
        right(15)
    forward(size*0.28)    
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
def F(size):
    left(90)
    forward(size)
    right(90)
    forward(size/2)
    backward(size/2)
    right(90)
    forward(size/2)
    left(90)
    forward(size/2)
def G(size):
    forward(size/2)
    left(90)
    forward(size/2)
    left(90)
    forward(size/4)
    penup()
    forward(size/4)
    pendown()
    left(90)
    forward(size/2)
    right(180)
    forward(size)
    right(90)
    forward(size/2)
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
def I(size):
    forward(size/2)
    backward(size/4)
    left(90)
    forward(size)
    left(90)
    forward(size/4)
    left(180)
    forward(size/2)
def J(size):
    forward(size/2)
    left(90)
    forward(size)
    left(90)
    forward(size/4)
    right(180)
def K(size):
    left(90)
    forward(size)
    backward(size/2)
    right(90)
    forward(size*0.23)
    left(65)
    forward(size*0.55)
    backward(size*0.55)
    right(65*2)
    forward(size*0.55)
    left(65)
def L(size):
    left(90)
    forward(size)
    backward(size)
    right(90)
    forward(size/2)
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
def N(size):
    left(90)
    forward(size)
    right(90)
    right(63.43)
    forward(size/0.894)
    left(63.43)
    left(90)
    forward(size)
    right(90)
def O(size):
    forward(size/2)
    left(90)
    forward(size)
    left(90)
    forward(size/2)
    left(90)
    forward(size)
    left(90)
def P(size):
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
def Q(size):
    forward(size/2)
    left(90)
    forward(size)
    left(90)
    forward(size/2)
    left(90)
    forward(size)
    left(90)
    forward(size/3)
    right(45)
    forward(size/5)
    backward(size*2/5)
    forward(size/5)
    left(45)
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
def V(size):
    left(90)
    penup()
    forward(size)
    right(90)
    pendown()
    right(math.degrees(math.atan(4)))
    forward(math.sqrt(size*size*1.0625))
    left(math.degrees(math.atan(4))*2)
    forward(math.sqrt(size*size*1.0625))
    right(math.degrees(math.atan(4)))
def W(size):
    penup()
    left(90)
    forward(size)
    right(180)
    pendown()
    left(9.46)
    forward(size/0.9864)
    left(160.72)
    forward(size/2*0.9864)
    right(160.72)
    forward(size/2*0.9864)
    left(160.72)
    forward(size/0.9864)
    left(9.46)
    right(90)
def X(size):
    left(63.43)
    forward(size/0.894)
    right(63.43)
    penup()
    backward(size/2)
    pendown()
    right(63.43)
    forward(size/0.894)
    left(63.43)
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
def Z(size):
    forward(size/2)
    backward(size/2)
    left(63.43)
    forward(size/0.894)
    right(63.43)
    backward(size/2)
def KA(size):
    # క
    dis_ratio = 0.03

    left(90)
    penup()
    forward(size/8)
    right(90)
    right(32)
    pendown()

    for x in range(0, 12):
        forward(size*dis_ratio)
        left(fibsequence[x])
    
    forward(size*0.09)

    for x in range(0, 16):
        forward(size*dis_ratio)
        left(fibsequence[x])

    for x in range(0, 16):
        forward(size*dis_ratio)
        left(fibsequence[15-x])

    for x in range(0, 16):
        forward(size*dis_ratio)
        right(fibsequence[x])

    for x in range(0, 16):
        forward(size*dis_ratio)
        right(fibsequence[15-x])
    
    left(45)
    forward(size*0.3)
    backward(size*0.3)
    left(90)
    forward(size*0.2)
    backward(size*0.2)
    right(135)

    for x in range(0, 12):
        forward(size*dis_ratio)
        right(fibsequence[x])

    left(32)
def PA(size):
    # ప్ప
    dis_ratio = 0.03
    penup()
    forward(size*0.25)
    left(90)
    forward(size/8)
    left(90)
    left(32)
    pendown()
    for x in range(0, 12):
        forward(size*dis_ratio)
        right(fibsequence[x])
    pass

    for x in range(0, 16):
        forward(size*dis_ratio)
        right(fibsequence[x])

    for x in range(0, 16):
        forward(size*dis_ratio)
        right(fibsequence[15-x])

    for x in range(0, 13):
        forward(size*dis_ratio)
        right(fibsequence[x])
    right(2.5)

    forward(size*0.1)

    left(2.5)
    for x in range(0, 13):
        forward(size*dis_ratio)
        left(fibsequence[x])

    for x in range(0, 16):
        forward(size*dis_ratio)
        left(fibsequence[15-x])

    for x in range(0, 16):
        forward(size*dis_ratio)
        left(fibsequence[x])
    forward(size*0.3)

    penup()
    forward(size*0.1)
    pendown()
    right(90)
    right(45)
    forward(size*0.3)
    backward(size*0.3)
    left(90)
    forward(size*0.2)
    backward(size*0.2)
    right(135)

    penup()
    forward(size*0.8)
    pendown()
    right(70)
    for x in range(0, 20):
        forward(size*0.01)
        right(1)
    forward(size*0.6)
    for x in range(0, 16):
        forward(size*dis_ratio)
        right(fibsequence[x])
 
    for x in range(0, 13):
        forward(size*dis_ratio)
        right(fibsequence[x])
    right(2.5)

    forward(size*0.1)

    left(2.5)
    for x in range(0, 13):
        forward(size*dis_ratio)
        left(fibsequence[x])
    
    for x in range(0, 18):
        forward(size*dis_ratio*0.6)
        left(5)

    for x in range(0, 18):
        forward(size*dis_ratio*0.6)
        left(5)

    left(2.5)
    for x in range(0, 15):
        forward(size*dis_ratio*1.1)
        left(fibsequence[x])
    right(74)
#endregion

#region Change colour to a random new colour
colours = ["black", "green", "red", "blue", "purple", "magenta", "turquoise", "violet", "skyblue", "silver"] 
def ColourChanger():
    color(colours[random.randint(0, 9)])
#endregion

#region
def LetterCreator(char):
    match char:
        case 'A':
            ColourChanger()
            A(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'B':
            ColourChanger()
            B(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'C':
            ColourChanger()
            C(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'D':
            ColourChanger()
            D(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'E':
            ColourChanger()
            E(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'F':
            ColourChanger()
            F(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'G':
            ColourChanger()
            G(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'H':
            ColourChanger()
            H(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'I':
            ColourChanger()
            I(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'J':
            ColourChanger()
            J(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'K':
            ColourChanger()
            K(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'L':
            ColourChanger()
            L(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'M':
            ColourChanger()
            M(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'N':
            ColourChanger()
            N(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'O':
            ColourChanger()
            O(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'P':
            ColourChanger()
            P(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'Q':
            ColourChanger()
            Q(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'R':
            ColourChanger()
            R(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'S':
            ColourChanger()
            S(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'T':
            ColourChanger()
            T(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'U':
            ColourChanger()
            U(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'V':
            ColourChanger()
            V(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'W':
            ColourChanger()
            W(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'X':
            ColourChanger()
            X(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'Y':
            ColourChanger()
            Y(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case 'Z':
            ColourChanger()
            Z(Variables_Mandelbrot.cs)
            n_along(Variables_Mandelbrot.cs)
        case ' ':
            n_down(Variables_Mandelbrot.cs)
        case other:
            pass
#endregion

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