from turtle import *
import Variables_Mandelbrot
#region Move cursor
#Move to next character along
def n_along(size):
    Variables_Mandelbrot.cursor_x = Variables_Mandelbrot.cursor_x + size * 0.7
    penup()
    goto(Variables_Mandelbrot.cursor_x, Variables_Mandelbrot.cursor_y)
    pendown()

#Move to next line down
def n_down(size):
    Variables_Mandelbrot.cursor_x = Variables_Mandelbrot.x_indendation
    Variables_Mandelbrot.cursor_y = Variables_Mandelbrot.cursor_y - size *1.2
    penup()
    goto(Variables_Mandelbrot.cursor_x, Variables_Mandelbrot.cursor_y)
    pendown()
#endregion
