#функция вывода
import numpy as np
import turtle as t

class Plotter:
    def __init__(self,width,height):
        self.wn = t.Screen()
        self.wn.title('Plotter')
        self.wn.bgcolor("White")
        self.wn.setup(width=width,height=height)
        self.width = width
        self.height = height
        self.wn.tracer(0)

        def plot(self, x, y, color):  # функция вывода любого графика через x,y
            min_x = x[0]
            max_x = x[0]
            for kx in x:  # масштабируем окошко по х
                if kx > max_x:
                    max_x = kx
                if kx < min_x:
                    min_x = kx

            min_y = y[0]
            max_y = y[0]
            for ky in y:  # масштабируем окошко по y
                if ky > max_y:
                    max_y = ky
                if ky < min_y:
                    min_y = ky

            tmp = t.Turtle()
            tmp.penup()
            tmp.color(color)
            tmp.goto(-self.width / 2, 0)
            tmp.pendown()

            for i in range(x.size):
                loc_x = (x[i] - min_x) / (max_x - min_x) * self.width - self.width / 2
                loc_y = (y[i] - min_y) / (max_y - min_y) * self.height - self.height / 2
                tmp.goto(loc_x, loc_y)
            tmp.penup()