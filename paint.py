from tkinter import *


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.color = "black"
        self.brush_size = 2
        self.setUI()

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

