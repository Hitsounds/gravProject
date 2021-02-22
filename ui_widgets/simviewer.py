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
        self.f = Figure(figsize=(5,5), dpi=100)
        #1st 1x1 subplot
        self.plot = self.f.add_subplot(111)

        #Centre axis on (0,0)
        self.plot.spines['left'].set_position('zero')
        self.plot.spines['bottom'].set_position('zero')
        #Hide unnecessary spines
        self.plot.spines['right'].set_color('none')
        self.plot.spines['top'].set_color('none')
        
        self.plot.xaxis.set_ticks_position('bottom')
        self.plot.yaxis.set_ticks_position('left')

        self.lines = []

        #Sample plot until simulation implemented
        self.plot.set_title("Distances in Meters")
        #self.line = self.plot.plot([-1000,-100,-10,0,10,100,1000],[-1000,-100,-10,0,10,100,1000])[0]
        #self.lineni = self.plot.plot([-1000,-100,-10,0,10,100,1000],[1000, 100, 10, 0, -10, -100, -1000])[0]

        self.canvas = FigureCanvasTkAgg(self.f, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        #self.update_line(100,200)

    def set_number_of_lines(self, numberOfLines):
        '''
        Set the number of lines
        which is equal to the number of bodies
        '''
        for i in self.lines:
            i.remove()
        self.lines = []
        for i in range(numberOfLines):
            self.lines.append(self.plot.plot([],[],linestyle="-" ,marker="o", markevery=1)[0])
        self.canvas.draw()

    def clear_line(self, index):
        '''
        Clears data from a line specified by its index
        '''
        self.lines[index].set_xdata([])
        self.lines[index].set_ydata([])
        self.canvas.draw()

    def clear_all_lines(self):
        '''
        Clears data from all lines
        '''
        for i in range(len(self.lines)):
            self.clear_line(i)

    def update_line(self, index, x_values, y_values):
        '''Append new data to a line,
        recalculate the limits of the graph,
        scale the graph according to the new limits
        and then draw the new graph to the output
        '''
        x_data = self.lines[index].get_xdata()
        y_data = self.lines[index].get_ydata()
        if len(x_data) != 0:
            self.lines[index].set_markevery(len(x_data))
        self.lines[index].set_xdata(numpy.append(x_data,x_values))
        self.lines[index].set_ydata(numpy.append(y_data,y_values))
        self.plot.relim()
        self.f.gca().set_aspect('equal', adjustable='box')
        self.plot.autoscale_view()
        self.canvas.draw()

    def easy_update(self, new_state):
        '''
        Easy inteface which accepts the state output from a simulator engine direcly
        to update the graph
        '''
        for i in range(len(new_state)):
            pos = new_state[i]["pos"]
            self.update_line(i,pos[0],pos[1])    
