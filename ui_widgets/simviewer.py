import tkinter as tk

import numpy

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class SimulationViewer(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="red")
        test = tk.Label(self, text="SimulationViewer" )
        test.pack()
        f = Figure(figsize=(5,5), dpi=100)
        self.a = f.add_subplot(111)

        #Centre axis on (0,0)
        self.a.spines['left'].set_position('zero')
        self.a.spines['bottom'].set_position('zero')
        self.a.spines['right'].set_color('none')
        self.a.spines['top'].set_color('none')
        self.a.xaxis.set_ticks_position('bottom')
        self.a.yaxis.set_ticks_position('left')

        #Sample plot until simulation implemented
        self.line, = self.a.plot([-100,1,2,3,4,5,6,7,8],[-50,5,6,1,3,8,9,3,5])
        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.update_line(100,200)


    def clear_line(self):
        self.line.set_xdata([])
        self.line.set_ydata([])
        self.canvas.draw()

    def update_line(self, x_values, y_values):
        '''Append new data to line,
        recalculate the limits of the graph,
        scale the graph according to the new limits
        and then draw the new graph to the output
        '''
        self.line.set_xdata(numpy.append(self.line.get_xdata(),x_values))
        self.line.set_ydata(numpy.append(self.line.get_ydata(),y_values))
        self.a.relim()
        self.a.autoscale_view()
        self.canvas.draw()
        

