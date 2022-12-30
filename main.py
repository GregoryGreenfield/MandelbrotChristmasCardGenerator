# turtle is a 2d graphiVariables_Mandelbrot.cs module
from CharactersTreeSnowflake import *
from turtle import *
pensize(2.5)
shape('turtle')

penup()
goto(Variables_Mandelbrot.cursor_x, Variables_Mandelbrot.cursor_y)
pendown()
#stops refreshing screen
tracer(0, 0)
        
#region Function calls
#message can be up to 9 words long, and each word is 18 characters or shorter.
nameMessage = 'MERRY CHRISTMAS HOMER SIMPSON'
for c in nameMessage:
    LetterCreator(c) 
#endregion

#region Snowflakes/Trees
tracer(0,0)
pensize(1)
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

penup()
goto(200, 0)
pendown()
left(90)
tree(35, 6, 30)
right(90)

#creates multiple small silver snowflakes
for x in range(0,100):
    penup()
    goto(random.randint(-380,380),random.randint(-350,350))
    color("silver")
    pendown()
    create_snowflake(3, 10)
#endregion

hideturtle()
update()
penup()
goto(0,0)
pendown()
mainloop()