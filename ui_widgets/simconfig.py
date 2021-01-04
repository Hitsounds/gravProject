import tkinter as tk

class SimConfig(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="purple")

        #Title of widget
        title = tk.Label(self, text="Simulation Settings")
        title.pack(side="top")

        #Settings category selection
        self.choice = tk.StringVar(self)
        choices = {"General", "Central Body"}
        self.choice.set("General")
        self.configMenu = tk.OptionMenu(self, self.choice, *choices)
        self.configMenu.pack(side="top")


        #Canvas is used here to make the widget scrollable as we may have more options than space
        self.options = tk.Canvas(self, bg="pink")
        self.options.pack(side="left", fill="both",expand=1)

        #Scrollbar if necessary
        yscrollbar = tk.Scrollbar(self, orient="vertical", command=self.options.yview)
        yscrollbar.pack(side="right", fill="y")

    #def add_body(self):


        
        
