import io
import os
import urllib
import urllib.request
import webbrowser
import wave

from PIL import ImageTk, Image

from retrieveSoundsAPI import *
from soundImprover import *
from readCSV import *

import simpleaudio as sa

bg1 = "#BA93D6" # Principal
bg2 = "#CDB3DF" # Screen
bg3 = "white" # Container
bg4 = "#41056D" # Container letter

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("AHSC")
        self.geometry("1000x600")

        self.top_frame = tk.Frame(self)
        self.top_frame.configure(bg=bg1)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        self.down_frame = tk.Frame(self)
        self.down_frame.configure(bg=bg1)
        self.down_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.title_label = tk.Label(self.top_frame, text="AHSC: Automatic Horror Sound Classification", font=("Arial", 15), fg="black", bg=bg1)
        self.title_label.configure(justify="center")
        self.title_label.grid(row=0, column=1, padx=150)

        self.info_label = tk.Label(self.top_frame, text="Click the sound image to listen to the sound!",
                                    font=("Arial", 8), fg="black", bg=bg1)
        self.info_label.configure(justify="center")
        self.info_label.grid(row=1, column=1, pady=5)

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        self.b_frame = tk.Frame(self.main_frame, width=100)
        self.b_frame.configure(bg=bg1)
        self.b_frame.pack(side=tk.LEFT, fill=tk.Y)

        scrollbar = tk.Scrollbar(self.b_frame)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        canvas = tk.Canvas(self.b_frame, yscrollcommand=scrollbar.set, width=150)
        canvas.configure(bg=bg1)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=canvas.yview)

        self.button_frame = tk.Frame(canvas)
        self.button_frame.configure(bg=bg1)
        canvas.create_window((0, 0), window=self.button_frame, anchor=tk.NW)

        self.screen_frame = tk.Frame(self.main_frame)
        self.screen_frame.configure(bg=bg2)
        self.screen_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.category_label = tk.Label(self.button_frame, text="Categories:", font=("Arial", 15), fg="black", bg=bg1)
        self.category_label.pack(pady=10, padx=20)

        self.login_label = tk.Label(self.top_frame, text="Login", fg="black", font=("Arial", 10))
        self.login_label.grid(row=0, column=2, pady=10)
        self.login_label.configure(background=bg1, cursor="hand2", justify="center")
        self.login_label.bind("<Button-1>", show_login)

        ################################### LOGO ###############################################
        # Load the image
        self.image = Image.open("logo.png")  # Replace with the path to your image
        self.image = self.image.resize((80, 80))  # Resize the image as desired
        self.photo = ImageTk.PhotoImage(self.image)

        # Create a label to display the image
        self.image_label = tk.Label(self.top_frame, image=self.photo)
        self.image_label.grid(row=0, column=0, sticky="nw", padx=30, pady=10)

        ##################################### ABOUT BUTTON #############################################
        self.aboutButton = tk.Button(self.down_frame, text="About", font=("Arial", 10), command=self.show_about,
                                     background=bg1, relief=tk.FLAT, borderwidth=0, fg="black")
        self.aboutButton.pack(side=tk.TOP, pady=5)
        ################################### CATEGORY BUTTONS ###############################################
        self.button1 = tk.Button(self.button_frame, text="Alarm", command=self.show_screen1, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button1.pack()

        self.button2 = tk.Button(self.button_frame, text="Insect", command=self.show_screen2, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button2.pack()

        self.button3 = tk.Button(self.button_frame, text="Respiratory", command=self.show_screen3, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button3.pack()

        self.button4 = tk.Button(self.button_frame, text="Screaming", command=self.show_screen4, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button4.pack()

        self.button5 = tk.Button(self.button_frame, text="Bell", command=self.show_screen5, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button5.pack()

        self.button6 = tk.Button(self.button_frame, text="Bird", command=self.show_screen6, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button6.pack()

        self.button7 = tk.Button(self.button_frame, text="Bowed String Instruments", command=self.show_screen7, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button7.pack()

        self.button8 = tk.Button(self.button_frame, text="Creature", command=self.show_screen8, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button8.pack()

        self.button9 = tk.Button(self.button_frame, text="Door / Window", command=self.show_screen9, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button9.pack()

        self.button10 = tk.Button(self.button_frame, text="Explosion", command=self.show_screen10, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button10.pack()

        self.button11 = tk.Button(self.button_frame, text="Fire", command=self.show_screen11, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button11.pack()

        self.button12 = tk.Button(self.button_frame, text="Guitar", command=self.show_screen12, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button12.pack()

        self.button13 = tk.Button(self.button_frame, text="Gunshot", command=self.show_screen13, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button13.pack()

        self.button14 = tk.Button(self.button_frame, text="Footsteps", command=self.show_screen14, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button14.pack()

        self.button15 = tk.Button(self.button_frame, text="House", command=self.show_screen15, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button15.pack()

        self.button16 = tk.Button(self.button_frame, text="Howl", command=self.show_screen16, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button16.pack()

        self.button17 = tk.Button(self.button_frame, text="Interferences", command=self.show_screen17, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button17.pack()

        self.button18 = tk.Button(self.button_frame, text="Keyboard Instruments", command=self.show_screen18, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button18.pack()

        self.button19 = tk.Button(self.button_frame, text="Laughter", command=self.show_screen19, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button19.pack()

        self.button20 = tk.Button(self.button_frame, text="Motor", command=self.show_screen20, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button20.pack()

        self.button21 = tk.Button(self.button_frame, text="NIghtmare", command=self.show_screen21, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button21.pack()

        self.button22 = tk.Button(self.button_frame, text="Rain", command=self.show_screen22, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button22.pack()

        self.button23 = tk.Button(self.button_frame, text="Telephone", command=self.show_screen23, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button23.pack()

        self.button24 = tk.Button(self.button_frame, text="Tools", command=self.show_screen24, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button24.pack()

        self.button25 = tk.Button(self.button_frame, text="Whispers", command=self.show_screen25, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button25.pack()

        self.button26 = tk.Button(self.button_frame, text="Wind", command=self.show_screen26, background=bg1,
                                 relief=tk.FLAT, borderwidth=0, fg="black")
        self.button26.pack()
        #########################################################################################

        self.current_screen = None

        # Configure the canvas to scroll the inner frame
        canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

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

    def show_screen2(self):
        interface.count = 2
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen3(self):
        interface.count = 3
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen4(self):
        interface.count = 4
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen5(self):
        interface.count = 5
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen6(self):
        interface.count = 6
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen7(self):
        interface.count = 7
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen8(self):
        interface.count = 8
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen9(self):
        interface.count = 9
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen10(self):
        interface.count = 10
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen11(self):
        interface.count = 11
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen12(self):
        interface.count = 12
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen13(self):
        interface.count = 13
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen14(self):
        interface.count = 14
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen15(self):
        interface.count = 15
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen16(self):
        interface.count = 16
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen17(self):
        interface.count = 17
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen18(self):
        interface.count = 18
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen19(self):
        interface.count = 19
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen20(self):
        interface.count = 20
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen21(self):
        interface.count = 21
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen22(self):
        interface.count = 22
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen23(self):
        interface.count = 23
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen24(self):
        interface.count = 24
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen25(self):
        interface.count = 25
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_screen26(self):
        interface.count = 26
        self.clear_screen()
        self.current_screen = Screen(self.screen_frame)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def clear_screen(self):
        if self.current_screen:
            self.current_screen.pack_forget()

    #########################################################################################

################################ OTHER FUNCTIONS ##################################################
def show_login(self):
    webbrowser.open("https://freesound.org/home/login/")

def mp3towav(sound):
    wavsound = sound + '.wav'
    return wavsound
def playSound(sound):
    # Obtain url from the sound
    sound_url = sound['previews']['preview-hq-mp3']
    store_name1 = sound_url.split('/')[-1]
    sound_dir = "../dataset/interfaceSounds/" + store_name1
    urllib.request.urlretrieve(sound_url, sound_dir)
    store_name2 = mp3towav(store_name1)
    sound_dir2 = "../dataset/interfaceSounds/" + store_name2

    improveSound(sound_dir, sound_dir2)
    wave.open(sound_dir2)
    wave_obj = sa.WaveObject.from_wave_file(sound_dir2)
    play_obj = wave_obj.play()

def downloadSound(sound):
    webbrowser.open(sound['download'])
def getSoundImage(sound):
    image_url = sound['images']['waveform_m']
    image_data = urllib.request.urlopen(image_url).read()
    image = Image.open(io.BytesIO(image_data))
    photo = ImageTk.PhotoImage(image)

    return photo

def moreInfo(sound):
    webbrowser.open(sound["url"])

def seeLicense(sound):
    webbrowser.open(sound["license"])

def delete_all_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()
###################################################################################################
def getSounds(inner_frame, current_page_data):

    # Show the data
    for sound in current_page_data:
        response = retrieveSound(sound['sound_id'])
        container = tk.Frame(inner_frame)
        container.configure(bg=bg3)
        container.pack(pady=20, padx=10, fill=tk.X)

        # Load the image
        photo = getSoundImage(response)

        # Create a label to display the image
        image_label = tk.Label(container, image=photo)
        image_label.image = photo
        image_label.grid(row=0, column=0, sticky="nw", padx=10, pady=20)
        image_label.bind("<Button-1>", lambda event, sound=response: playSound(sound))

        name_label = tk.Label(container, text=response['name'])
        name_label.configure(fg=bg4, background=bg3)
        name_label.grid(row=0, column=1, padx=10, pady=20)

        username_label = tk.Label(container, text="User: " + response['username'])
        username_label.configure(fg=bg4, background=bg3)
        username_label.grid(row=1, column=1, padx=10, pady=20)

        icon_path = "download.png"
        svg_image = Image.open(icon_path)
        svg_image = svg_image.resize((20, 20))
        icon = ImageTk.PhotoImage(svg_image)
        download_label = tk.Label(container, image=icon)
        download_label.image = icon
        download_label.config(cursor="hand2")
        download_label.bind("<Button-1>", lambda event, sound=response: downloadSound(sound))
        download_label.grid(row=0, column=2, padx=10, pady=20)

        info_label = tk.Label(container, text="More info")
        info_label.grid(row=0, column=3, padx=10, pady=20)
        info_label.config( cursor="hand2", fg=bg4, background=bg3)
        info_label.bind("<Button-1>", lambda event, sound=response: moreInfo(sound))

        tags = []
        i = 2
        numcat1 = int(sound['category_1'])
        cat1 = classesAndLabels[numcat1]
        prob1 = float(sound['prob_1'])
        prob1 = round((prob1 * 100), 2)

        numcat2 = int(sound['category_2'])
        cat2 = classesAndLabels[numcat2]
        prob2 = float(sound['prob_2'])
        prob2 = round((prob2 * 100), 2)

        numcat3 = int(sound['category_3'])
        cat3 = classesAndLabels[numcat3]
        prob3 = float(sound['prob_3'])
        prob3 = round((prob3 * 100), 2)

        numcat4 = int(sound['category_4'])
        cat4 = classesAndLabels[numcat4]
        prob4 = float(sound['prob_4'])
        prob4 = round((prob4 * 100), 2)

        numcat5 = int(sound['category_5'])
        cat5 = classesAndLabels[numcat5]
        prob5 = float(sound['prob_5'])
        prob5 = round((prob5 * 100), 2)

        tags.append(str(cat1) + ' - ' + str(prob1) + '%')
        tags.append(str(cat2) + ' - ' + str(prob2) + '%')
        tags.append(str(cat3) + ' - ' + str(prob3) + '%')
        tags.append(str(cat4) + ' - ' + str(prob4) + '%')
        tags.append(str(cat5) + ' - ' + str(prob5) + '%')

        for tag in tags:
            tags_label = tk.Label(container, text=tag)
            tags_label.configure(fg=bg4, background=bg3)
            tags_label.grid(row=1, column=i, pady=20, padx=10)
            i += 1

        license_label = tk.Label(container, text="License")
        license_label.configure(cursor="hand2", fg=bg4, background=bg3)
        license_label.grid(row=1, column=0, padx=10, pady=20)
        license_label.bind("<Button-1>", lambda event, sound=response: seeLicense(sound))

##################################### SCREENS ####################################################
class Screen(tk.Frame):
    def get_current_page_data(self):
        self.start_index = (self.current_page - 1) * self.limit
        self.end_index = self.start_index + self.limit
        return self.sounds[self.start_index:self.end_index]

    def show_previous_page(self):
        self.current_page -= 1
        if self.current_page < 1:
            self.current_page = 1
        self.current_page_data = self.get_current_page_data()
        delete_all_widgets(self.inner_frame)
        getSounds(self.inner_frame, self.current_page_data)
        button_frame = tk.Frame(self.inner_frame, bg=bg2)
        button_frame.pack(side=tk.BOTTOM, fill=tk.BOTH)

        previous_button = tk.Button(button_frame, text="Previous Page", command=self.show_previous_page)
        previous_button.grid(row=0, column=1, padx=10, pady=10, sticky="nw")

        next_button = tk.Button(button_frame, text="Next Page", command=self.show_next_page)
        next_button.grid(row=0, column=2, pady=10)
    def show_next_page(self):
        self.current_page += 1
        if self.current_page > self.total_pages:
            self.current_page = 1
        self.current_page_data = self.get_current_page_data()
        delete_all_widgets(self.inner_frame)
        getSounds(self.inner_frame, self.current_page_data)
        button_frame = tk.Frame(self.inner_frame, bg=bg2)
        button_frame.pack(side=tk.BOTTOM, fill=tk.BOTH)

        previous_button = tk.Button(button_frame, text="Previous Page", command=self.show_previous_page)
        previous_button.grid(row=0, column=1, padx=10, pady=10, sticky="nw")

        next_button = tk.Button(button_frame, text="Next Page", command=self.show_next_page)
        next_button.grid(row=0, column=2, pady=10)

    def __init__(self, master):
        super().__init__(master)
        self.configure(bg=bg2)

        # Create a canvas widget
        canvas = tk.Canvas(self, bg=bg2)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar and associate it with the canvas
        scrollbar = tk.Scrollbar(self, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the content
        self.inner_frame = tk.Frame(canvas, bg=bg2)
        self.inner_frame.pack()
        canvas.create_window((0, 0), window=self.inner_frame, anchor=tk.NW)

        # Create a frame inside the canvas to hold the about content
        about_frame = tk.Frame(canvas, bg=bg2)
        about_frame.pack()
        canvas.create_window((0, 0), window=about_frame, anchor=tk.NW)

        # Create a horizontal scroll bar
        scrollbar = tk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
        scrollbar.pack(fill=tk.X, side=tk.BOTTOM)
        canvas.configure(xscrollcommand=scrollbar.set)

        self.sounds = []

        if(interface.count == 0):       # About Screen
            label = tk.Label(about_frame, text="This project is called AHSC: Automatic Horror Sound Classification and it's about to create a software that classifies different horror sounds. \nBasically, we get horror sounds from Freesound (https://freesound.org/) and we create a software application. \nThis application classifies these sounds into different categories. \n\nAHSC is an innovative project developed as part of the Music Technology Workshop elective course for ICT engineering degrees at UPF. \nThe aim of this project is to develop a software application based on the 'Freesound' website to classify horror sounds by using a new \ntagging system created by us to classify these horror sounds automatically in subcategories. \n\nWith almost 12000 available horror-related sounds on the website without specific tags, \nthis project proposes a solution that involves using metadata and implementing classification algorithms to generate subcategories, \nwhich will allow for more accurate and specific searches. \n\nTo achieve this, the project employs the Python programming language and the Pycharm IDE, along with the powerful 'Essentia' \nlibraries that help with sound analysis and descriptor extraction, and the 'Scikit-learn' library for machine learning techniques.")
            label.configure(font=("Arial", 10), background=bg2, fg="black")
            label.pack(anchor='w', pady=10, padx=10)

            label2 = tk.Label(about_frame, text="Víctor Alcaide \nSara Barbé \nLaia Duch \nNaiara Garmendia \nArnau Adan \nCristina Mendoza")
            label2.configure(font=("Arial", 10), background=bg2, fg="black")
            label2.pack(pady=10, padx=10)

        elif(interface.count == 1):     # Alarm Screen
            self.sounds = alarmSounds
        elif(interface.count == 2):     # Insect Screen
            self.sounds = insectSounds
        elif (interface.count == 3):    # Respiratory Screen
            self.sounds = respiratorySounds
        elif (interface.count == 4):    # Screaming Screen
            self.sounds = screamingSounds
        elif (interface.count == 5):
            self.sounds = bellSounds
        elif (interface.count == 6):
            self.sounds = birdSounds
        elif (interface.count == 7):
            self.sounds = bowedSounds
        elif (interface.count == 8):
            self.sounds = creatureSounds
        elif (interface.count == 9):
            self.sounds = doorSounds
        elif (interface.count == 10):
            self.sounds = explosionSounds
        elif (interface.count == 11):
            self.sounds = fireSounds
        elif (interface.count == 12):
            self.sounds = guitarSounds
        elif (interface.count == 13):
            self.sounds = gunshotSounds
        elif (interface.count == 14):
            self.sounds = footSounds
        elif (interface.count == 15):
            self.sounds = houseSounds
        elif (interface.count == 16):
            self.sounds = howlSounds
        elif (interface.count == 17):
            self.sounds = interferencesSounds
        elif (interface.count == 18):
            self.sounds = keyboardSounds
        elif (interface.count == 19):
            self.sounds = laughSounds
        elif (interface.count == 20):
            self.sounds = motorSounds
        elif (interface.count == 21):
            self.sounds = nightmareSounds
        elif (interface.count == 22):
            self.sounds = rainSounds
        elif (interface.count == 23):
            self.sounds = telephoneSounds
        elif (interface.count == 24):
            self.sounds = toolSounds
        elif (interface.count == 25):
            self.sounds = whisperSounds
        elif (interface.count == 26):
            self.sounds = windSounds

        self.sounds = orderList(self.sounds) # Order the sounds from high to low prob_1

        self.limit = 5
        self.total_pages = (len(self.sounds) + self.limit - 1) // self.limit
        self.current_page = 1
        self.current_page_data = self.get_current_page_data()

        getSounds(self.inner_frame, self.current_page_data)

        # Create the buttons to change between pages
        button_frame = tk.Frame(self.inner_frame, bg=bg2)
        button_frame.pack(side=tk.BOTTOM, fill=tk.BOTH)

        previous_button = tk.Button(button_frame, text="Previous Page", command=self.show_previous_page)
        previous_button.grid(row=0, column=1, padx=10, pady=10, sticky="nw")

        next_button = tk.Button(button_frame, text="Next Page", command=self.show_next_page)
        next_button.grid(row=0, column=2, pady=10)

        # Configure the canvas to scroll the inner frame
        self.inner_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
#########################################################################################

#### TO RUN THE INTERFACE ###############################################################
if __name__ == "__main__":
    interface = Interface()
    interface.mainloop()
