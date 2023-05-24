import tkinter as tk

from getListOfSounds import *

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("AHSC")
        self.geometry("1000x600")

        self.top_frame = tk.Frame(self)
        self.top_frame.configure(bg="#9D7CC5")
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        self.title_label = tk.Label(self.top_frame, text="AHSC: Automatic Horror Sound Classification", font=("Arial", 15), fg="black", bg="#9D7CC5")
        self.title_label.pack(pady=20)

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        self.button_frame = tk.Frame(self.main_frame, width=100)
        self.button_frame.configure(bg="#9D7CC5")
        self.button_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.screen_frame = tk.Frame(self.main_frame)
        self.screen_frame.configure(bg="#BE96EE")
        self.screen_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # self.scrollbar = tk.Scrollbar(self.screen_frame)
        # self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.category_label = tk.Label(self.button_frame, text="Categories:", font=("Arial", 15), fg="black", bg="#9D7CC5")
        self.category_label.pack(pady=10, padx=20)

        ################################### BUTTONS ###############################################
        self.button1 = tk.Button(self.button_frame, text="Screaming", command=self.show_screen1)
        self.button1.pack(pady=10, padx=20)

        self.button2 = tk.Button(self.button_frame, text="Car Engine", command=self.show_screen2)
        self.button2.pack(pady=10)

        self.button3 = tk.Button(self.button_frame, text="Owl", command=self.show_screen3)
        self.button3.pack(pady=10)

        self.button4 = tk.Button(self.button_frame, text="Knocking", command=self.show_screen4)
        self.button4.pack(pady=10)

        self.button5 = tk.Button(self.button_frame, text="Rain", command=self.show_screen5)
        self.button5.pack(pady=10)

        self.button6 = tk.Button(self.button_frame, text="Raven Bird", command=self.show_screen6)
        self.button6.pack(pady=10)

        self.button7 = tk.Button(self.button_frame, text="Violin", command=self.show_screen7)
        self.button7.pack(pady=10)
        #########################################################################################

        self.current_screen = None

    #################### FUNCTIONS TO SHOW THE SCREENS ##########################################
    def show_screen1(self):
        self.clear_screen()
        self.current_screen = Screen1(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)
        # self.current_screen.bind_scrollbar(self.scrollbar)

    def show_screen2(self):
        self.clear_screen()
        self.current_screen = Screen2(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)
        # self.current_screen.bind_scrollbar(self.scrollbar)

    def show_screen3(self):
        self.clear_screen()
        self.current_screen = Screen3(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)
        # self.current_screen.bind_scrollbar(self.scrollbar)

    def show_screen4(self):
        self.clear_screen()
        self.current_screen = Screen4(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)
        # self.current_screen.bind_scrollbar(self.scrollbar)

    def show_screen5(self):
        self.clear_screen()
        self.current_screen = Screen5(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)
        # self.current_screen.bind_scrollbar(self.scrollbar)
    def show_screen6(self):
        self.clear_screen()
        self.current_screen = Screen6(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)
        # self.current_screen.bind_scrollbar(self.scrollbar)
    def show_screen7(self):
        self.clear_screen()
        self.current_screen = Screen7(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)
        # self.current_screen.bind_scrollbar(self.scrollbar)
    def clear_screen(self):
        if self.current_screen:
            self.current_screen.pack_forget()
    #########################################################################################

##################################### SCREENS ####################################################
##################################### SCREAMING ##################################################
class Screen1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg="#BE96EE")

        # Create a canvas widget
        canvas = tk.Canvas(self, bg="#BE96EE")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar and associate it with the canvas
        scrollbar = tk.Scrollbar(self, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the content
        inner_frame = tk.Frame(canvas, bg="#BE96EE")
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        label = tk.Label(inner_frame, text="Here are displayed the sounds with the tag Screaming")
        label.configure(font=("Arial", 12), bg="#BE96EE")
        label.pack(pady=50, padx=50)

        screamingSounds = getSounds(screamingDir)
        for sound in screamingSounds:
            l = tk.Label(inner_frame, text=f"{sound} - {screamingDir.split('/')[-1]}")
            l.configure(font=("Arial", 12), bg="#BE96EE")
            l.pack()

        # Configure the canvas to scroll the inner frame
        inner_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

##################################### CAR ENGINE ################################################
class Screen2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg="#BE96EE")

        # Create a canvas widget
        canvas = tk.Canvas(self, bg="#BE96EE")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar and associate it with the canvas
        scrollbar = tk.Scrollbar(self, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the content
        inner_frame = tk.Frame(canvas, bg="#BE96EE")
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        label = tk.Label(inner_frame, text="Here are displayed the sounds with the tag Car engine")
        label.configure(font=("Arial", 12), bg="#BE96EE")
        label.pack(pady=50, padx=50)

        carSounds = getSounds(carDir)
        for sound in carSounds:
            l = tk.Label(inner_frame, text=f"{sound} - {carDir.split('/')[-1]}")
            l.configure(font=("Arial", 12), bg="#BE96EE")
            l.pack()

        # Configure the canvas to scroll the inner frame
        inner_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

##################################### OWL #####################################################
class Screen3(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg="#BE96EE")

        # Create a canvas widget
        canvas = tk.Canvas(self, bg="#BE96EE")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar and associate it with the canvas
        scrollbar = tk.Scrollbar(self, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the content
        inner_frame = tk.Frame(canvas, bg="#BE96EE")
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        label = tk.Label(inner_frame, text="Here are displayed the sounds with the tag Owl")
        label.configure(font=("Arial", 12), bg="#BE96EE")
        label.pack(pady=50, padx=50)

        owlSounds = getSounds(owlDir)
        for sound in owlSounds:
            l = tk.Label(inner_frame, text=f"{sound} - {owlDir.split('/')[-1]}")
            l.configure(font=("Arial", 12), bg="#BE96EE")
            l.pack()

##################################### KNOCKING ###############################################
class Screen4(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg="#BE96EE")

        # Create a canvas widget
        canvas = tk.Canvas(self, bg="#BE96EE")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar and associate it with the canvas
        scrollbar = tk.Scrollbar(self, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the content
        inner_frame = tk.Frame(canvas, bg="#BE96EE")
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        label = tk.Label(inner_frame, text="Here are displayed the sounds with the tag Knocking")
        label.configure(font=("Arial", 12), bg="#BE96EE")
        label.pack(pady=50, padx=50)

        knockSounds = getSounds(knockingDir)
        for sound in knockSounds:
            l = tk.Label(inner_frame, text=f"{sound} - {knockingDir.split('/')[-1]}")
            l.configure(font=("Arial", 12), bg="#BE96EE")
            l.pack()

##################################### RAIN ##################################################
class Screen5(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg="#BE96EE")

        # Create a canvas widget
        canvas = tk.Canvas(self, bg="#BE96EE")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar and associate it with the canvas
        scrollbar = tk.Scrollbar(self, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the content
        inner_frame = tk.Frame(canvas, bg="#BE96EE")
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        label = tk.Label(inner_frame, text="Here are displayed the sounds with the tag Rain")
        label.configure(font=("Arial", 12), bg="#BE96EE")
        label.pack(pady=50, padx=50)

        rainSounds = getSounds(rainDir)
        for sound in rainSounds:
            l = tk.Label(inner_frame, text=f"{sound} - {rainDir.split('/')[-1]}")
            l.configure(font=("Arial", 12), bg="#BE96EE")
            l.pack()

##################################### RAVEN BIRD ############################################
class Screen6(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg="#BE96EE")

        # Create a canvas widget
        canvas = tk.Canvas(self, bg="#BE96EE")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar and associate it with the canvas
        scrollbar = tk.Scrollbar(self, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the content
        inner_frame = tk.Frame(canvas, bg="#BE96EE")
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        label = tk.Label(inner_frame, text="Here are displayed the sounds with the tag Raven Bird")
        label.configure(font=("Arial", 12), bg="#BE96EE")
        label.pack(pady=50, padx=50)

        ravenSounds = getSounds(ravenDir)
        for sound in ravenSounds:
            l = tk.Label(inner_frame, text=f"{sound} - {ravenDir.split('/')[-1]}")
            l.configure(font=("Arial", 12), bg="#BE96EE")
            l.pack()

##################################### VIOLIN ################################################
class Screen7(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg="#BE96EE")

        # Create a canvas widget
        canvas = tk.Canvas(self, bg="#BE96EE")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar and associate it with the canvas
        scrollbar = tk.Scrollbar(self, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the content
        inner_frame = tk.Frame(canvas, bg="#BE96EE")
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        label = tk.Label(inner_frame, text="Here are displayed the sounds with the tag Violin")
        label.configure(font=("Arial", 12), bg="#BE96EE")
        label.pack(pady=50, padx=50)

        violinSounds = getSounds(violinDir)
        for sound in violinSounds:
            l = tk.Label(inner_frame, text=f"{sound} - {violinDir.split('/')[-1]}")
            l.configure(font=("Arial", 12), bg="#BE96EE")
            l.pack()
#########################################################################################

#### TO RUN THE INTERFACE ###############################################################
if __name__ == "__main__":
    interface = Interface()
    interface.mainloop()
