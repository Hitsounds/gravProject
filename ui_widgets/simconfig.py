import tkinter as tk
from functools import partial

class SimConfig(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="purple")


        self.settings = {
        "general":{
            "simulation_mode":["Simulation Mode","textChoice",tk.StringVar()],
            "timestep":["Timestep Ratio","numInput",tk.DoubleVar()]
        },
        "bodies":[]
        }
        self.settings["general"]["simulation_mode"][2].set("cycles")
        self.settings["general"]["timestep"][2].set("10")

        


        #Title of widget
        title = tk.Label(self, text="Simulation Settings")
        title.pack(side="top")

        #Settings category selection
        self.choice = tk.StringVar(self)
        self.body_edit_container = tk.Frame(self, background="#ffd3d3")
        self.choice.set("General")

        self.configMenu = tk.OptionMenu(self.body_edit_container, self.choice, {"placeholder"}, command=self.render_generalsettings)
        self.construct_optionmenu()
        self.configMenu.pack(side="left")

        self.add_button = tk.Button(self.body_edit_container, text="Add body" , command=self.add_body)
        self.add_button.pack(side="left")
        
        self.body_edit_container.pack(side="top")

        self.options = tk.Frame(self, bg="pink")
        self.options.pack(side="bottom", fill="both",expand=1)


        #Canvas is used here to make the widget scrollable as we may have more options than space
        #and also to make a clear distinction between the persistent menu and the settings which change depending on the item in the dropdown
        #self.options = tk.Canvas(self, bg="pink")
        #self.options.pack(side="bottom", fill="both",expand=1)

        #Scrollbar if necessary
        #yscrollbar = tk.Scrollbar(self.options, orient="vertical", command=self.options.yview)
        #yscrollbar.pack(side="right", fill="y")

        self.add_body()
        self.active_body = 0
        #Show general settings on first launch
        self.render_generalsettings()

    def positiveFloatValidation(self,test):
        try:
            if float(test) > 0:
                return True
        except Exception:
            return False
        else:
            return False

    def floatValidation(self,test):
        try:
            if test == "" or test == "-":
                return True
            float(test)
            return True
        except Exception:
            return False

    def construct_optionmenu(self):
        '''Constructs the dropdown menu of options
        '''
        menu = self.configMenu["menu"]
        menu.delete(0, "end")
        menu.add_command(label="General", command=partial(self.render_generalsettings))
        for i in range(0, len(self.settings["bodies"])):
            name = self.settings["bodies"][i]["nick"][2].get() or f"Body {i}"
            menu.add_command(label=name, command=partial(self.render_bodysettings, f"{i}"))
        self.configMenu.update()

    def add_body(self):
        '''Adds a body to the end of the settings
        '''
        #body template
        if len(self.settings["bodies"]) == 7:
            #do nothing if user tries to add more than 7 bodies
            return
        body_template = {
                "nick":["Nickname","stringInput",tk.StringVar()],
                "mass":["Mass (kg)","numInput",tk.DoubleVar()],
                "inital_x_pos":["x Position (m)","numInput",tk.DoubleVar()],
                "inital_y_pos":["y Position (m)","numInput",tk.DoubleVar()],
                "inital_x_speed":["x Speed (m/s)","numInput",tk.DoubleVar()],
                "inital_y_speed":["y Speed (m/s)","numInput",tk.DoubleVar()]
        }  
        #defaults
        body_template["mass"][2].set(10)
        body_template["inital_x_pos"][2].set(10)
        body_template["inital_y_pos"][2].set(10)
        body_template["inital_x_speed"][2].set(10)
        body_template["inital_y_speed"][2].set(10)
        self.settings["bodies"].append(body_template)
        self.construct_optionmenu()

    def remove_body(self, i):
        '''Removes the body with the index provided
        '''
        if len(self.settings["bodies"]) == 0:
            #Do nothing if user tries to delete last body
            return
        self.settings["bodies"].pop(i)
        self.construct_optionmenu()

    def clear_optionsFrame(self):
        '''
        Clears the Frame containing the options.
        Please write some new options to the frame after calling this.
        Don't want an empty frame after all.
        '''
        for widget in self.options.winfo_children():
            widget.destroy()

    def render_generalsettings(self):
        self.construct_optionmenu()
        self.choice.set("General")
        self.clear_optionsFrame()

        #Draw simulation mode selection
        label = tk.Label(self.options,text=self.settings["general"]["simulation_mode"][0])
        label.grid(row=0, column=0)
        simOptions = ("cycles","circles")
        mode_dropdown = tk.OptionMenu(self.options, self.settings["general"]["simulation_mode"][2], *simOptions)
        mode_dropdown.grid(row=0, column=1)

        #Draw TimeStep Selector
        label = tk.Label(self.options,text=self.settings["general"]["timestep"][0])
        label.grid(row=1, column=0)
        timeStepInput = tk.Entry(self.options, textvariable=self.settings["general"]["timestep"][2], validate="key")
        timeStepInput.configure(validatecommand=(timeStepInput.register(self.positiveFloatValidation), "%P"))
        timeStepInput.grid(row=1, column=1)

    def render_bodysettings(self, i):
        self.construct_optionmenu()
        name = self.settings["bodies"][int(i)]["nick"][2].get() or f"Body {i}"
        self.choice.set(name)
        self.active_body = int(i)
        self.clear_optionsFrame()

        #NickName
        label = tk.Label(self.options,text=self.settings["bodies"][self.active_body]["nick"][0])
        label.grid(row=0, column=0)
        nickInput = tk.Entry(self.options, textvariable=self.settings["bodies"][self.active_body]["nick"][2])
        nickInput.grid(row=0, column=1)

        #Mass
        label = tk.Label(self.options,text=self.settings["bodies"][self.active_body]["mass"][0])
        label.grid(row=1, column=0)
        massInput = tk.Entry(self.options, textvariable=self.settings["bodies"][self.active_body]["mass"][2], validate="key")
        massInput.configure(validatecommand=(massInput.register(self.positiveFloatValidation), "%P"))
        massInput.grid(row=1, column=1)

        #x pos
        label = tk.Label(self.options,text=self.settings["bodies"][self.active_body]["inital_x_pos"][0])
        label.grid(row=2, column=0)
        x_PosInput = tk.Entry(self.options, textvariable=self.settings["bodies"][self.active_body]["inital_x_pos"][2], validate="key")
        x_PosInput.configure(validatecommand=(x_PosInput.register(self.floatValidation), "%P"))
        x_PosInput.grid(row=2, column=1)

        #y pos
        label = tk.Label(self.options,text=self.settings["bodies"][self.active_body]["inital_y_pos"][0])
        label.grid(row=3, column=0)
        y_PosInput = tk.Entry(self.options, textvariable=self.settings["bodies"][self.active_body]["inital_y_pos"][2], validate="key")
        y_PosInput.configure(validatecommand=(y_PosInput.register(self.floatValidation), "%P"))
        y_PosInput.grid(row=3, column=1)

        #x speed
        label = tk.Label(self.options,text=self.settings["bodies"][self.active_body]["inital_x_speed"][0])
        label.grid(row=4, column=0)
        x_SpeedInput = tk.Entry(self.options, textvariable=self.settings["bodies"][self.active_body]["inital_x_speed"][2], validate="key")
        x_SpeedInput.configure(validatecommand=(x_SpeedInput.register(self.floatValidation), "%P"))
        x_SpeedInput.grid(row=4, column=1)

        #y speed
        label = tk.Label(self.options,text=self.settings["bodies"][self.active_body]["inital_y_speed"][0])
        label.grid(row=5, column=0)
        y_SpeedInput = tk.Entry(self.options, textvariable=self.settings["bodies"][self.active_body]["inital_y_speed"][2], validate="key")
        y_SpeedInput.configure(validatecommand=(y_SpeedInput.register(self.floatValidation), "%P"))
        y_SpeedInput.grid(row=5, column=1)

        #Remove body script
        def remove():
            self.render_generalsettings()
            self.remove_body(self.active_body)

        button = tk.Button(self.options, text="Remove Body", command=remove)
        button.grid(row=5, column=0)

    def get_settings(self):
        return self.settings
