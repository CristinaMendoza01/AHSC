import tkinter as tk
import webbrowser
import requests

from getListOfSounds import *
from retrieveSoundsAPI import *


def show_login(self):
    webbrowser.open("https://freesound.org/home/login/")

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("AHSC")
        self.geometry("1000x600")

        self.top_frame = tk.Frame(self)
        self.top_frame.configure(bg="#9D7CC5")
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        self.down_frame = tk.Frame(self)
        self.down_frame.configure(bg="#9D7CC5")
        self.down_frame.pack(side=tk.BOTTOM, fill=tk.X)

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

        self.category_label = tk.Label(self.button_frame, text="Categories:", font=("Arial", 15), fg="black", bg="#9D7CC5")
        self.category_label.pack(pady=10, padx=20)

        self.login_label = tk.Label(self.top_frame, text="Login", font=("Arial", 10))
        self.login_label.pack(pady=10)
        # Configuring the label as a link
        self.login_label.config(background="#9D7CC5", cursor="hand2")
        self.login_label.bind("<Button-1>", show_login)

        ################################### BUTTONS ###############################################
        self.aboutButton = tk.Button(self.down_frame, text="About", font=("Arial", 10), command=self.show_about,
                                     background="#9D7CC5", relief=tk.FLAT, borderwidth=0)
        self.aboutButton.pack(side=tk.TOP, pady=5)

        self.button1 = tk.Button(self.button_frame, text="Screaming", command=self.show_screen1, background="#9D7CC5", relief=tk.FLAT, borderwidth=0)
        self.button1.pack()

        self.button2 = tk.Button(self.button_frame, text="Car Engine", command=self.show_screen2, background="#9D7CC5", relief=tk.FLAT, borderwidth=0)
        self.button2.pack()

        self.button3 = tk.Button(self.button_frame, text="Owl", command=self.show_screen3, background="#9D7CC5", relief=tk.FLAT, borderwidth=0)
        self.button3.pack()

        self.button4 = tk.Button(self.button_frame, text="Knocking", command=self.show_screen4, background="#9D7CC5", relief=tk.FLAT, borderwidth=0)
        self.button4.pack()

        self.button5 = tk.Button(self.button_frame, text="Rain", command=self.show_screen5, background="#9D7CC5", relief=tk.FLAT, borderwidth=0)
        self.button5.pack()

        self.button6 = tk.Button(self.button_frame, text="Raven Bird", command=self.show_screen6, background="#9D7CC5", relief=tk.FLAT, borderwidth=0)
        self.button6.pack()

        self.button7 = tk.Button(self.button_frame, text="Violin", command=self.show_screen7, background="#9D7CC5", relief=tk.FLAT, borderwidth=0)
        self.button7.pack()
        #########################################################################################

        self.current_screen = None

    #################### FUNCTIONS TO SHOW THE SCREENS ##########################################
    count = 0
    def show_about(self):
        interface.count = 0
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen1(self):
        interface.count = 1
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)
        # self.current_screen.bind_scrollbar(self.scrollbar)

    def show_screen2(self):
        interface.count = 2
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)
        # self.current_screen.bind_scrollbar(self.scrollbar)

    def show_screen3(self):
        interface.count = 3
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)
        # self.current_screen.bind_scrollbar(self.scrollbar)

    def show_screen4(self):
        interface.count = 4
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)
        # self.current_screen.bind_scrollbar(self.scrollbar)

    def show_screen5(self):
        interface.count = 5
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)
        # self.current_screen.bind_scrollbar(self.scrollbar)

    def show_screen6(self):
        interface.count = 6
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)
        # self.current_screen.bind_scrollbar(self.scrollbar)

    def show_screen7(self):
        interface.count = 7
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)
        # self.current_screen.bind_scrollbar(self.scrollbar)
    def clear_screen(self):
        if self.current_screen:
            self.current_screen.pack_forget()

    #########################################################################################

################################ OTHER FUNCTIONS ##################################################
def obtainInfoSounds(dir):
    sounds = getSounds(dir)
    return sounds
###################################################################################################

##################################### SCREENS ####################################################
class Screen(tk.Frame):
    def __init__(self, master):
        global buttonClicked
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
        inner_frame.pack()
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        sounds = []
        if(interface.count == 0):
            label = tk.Label(inner_frame, text="This project is called AHSC: Automatic Horror Sound Classification and it's about to create a software that classifies different horror sounds. \nBasically, we get horror sounds from Freesound (https://freesound.org/) and we create a software application. \nThis application classifies these sounds into different categories. \n\nAHSC is an innovative project developed as part of the Music Technology Workshop elective course for ICT engineering degrees at UPF. \nThe aim of this project is to develop a software application based on the 'Freesound' website to classify horror sounds by using a new \ntagging system created by us to classify these horror sounds automatically in subcategories. \n\nWith almost 12000 available horror-related sounds on the website without specific tags, \nthis project proposes a solution that involves using metadata and implementing classification algorithms to generate subcategories, \nwhich will allow for more accurate and specific searches. \n\nTo achieve this, the project employs the Python programming language and the Pycharm IDE, along with the powerful 'Essentia' \nlibraries that help with sound analysis and descriptor extraction, and the 'Scikit-learn' library for machine learning techniques.")
            label.configure(font=("Arial", 10), background="#BE96EE")
            label.pack(anchor='w')

            label2 = tk.Label(inner_frame, text="Víctor Alcaide \nSara Barbé \nLaia Duch \nNaiara Garmendia \nArnau Adan \nCristina Mendoza")
            label2.configure(font=("Arial", 10), background="#BE96EE")
            label2.pack()

        elif(interface.count == 1):
            sounds = obtainInfoSounds(screamingDir)
        elif(interface.count == 2):
            sounds = obtainInfoSounds(carDir)
        elif (interface.count == 3):
            sounds = obtainInfoSounds(owlDir)
        elif (interface.count == 4):
            sounds = obtainInfoSounds(knockingDir)
        elif (interface.count == 5):
            sounds = obtainInfoSounds(rainDir)
        elif (interface.count == 6):
            sounds = obtainInfoSounds(ravenDir)
        elif (interface.count == 7):
            sounds = obtainInfoSounds(violinDir)

        for sound in sounds:
            response = retrieveSound(sound)
            button = tk.Button(inner_frame, text=response['name'])
            button.pack(pady=5, padx=5, anchor="w")

        # Configure the canvas to scroll the inner frame
        inner_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
#########################################################################################

#### TO RUN THE INTERFACE ###############################################################
if __name__ == "__main__":
    interface = Interface()
    # sounds = getSounds(violinDir)
    # for sound in sounds:
    #     res = retrieveSound(sound)
    #     print(res)
    interface.mainloop()
