import webbrowser

from callAPI import authorization_url
import tkinter as tk

global authcode

def openURL():
    webbrowser.open(authorization_url)
def get_token():
    global authcode
    authcode = code.get()
    window.destroy()

def login():
    webbrowser.open("https://freesound.org/home/login/")

def register():
    webbrowser.open("https://freesound.org/home/register/")

window = tk.Tk()
window.title("Authorization")
window.configure(bg="#CDB3DF")
window.geometry("500x400")

label = tk.Label(window, text="Hello! Please login or register in Freesound before using AHSC.")
label.configure(bg="#CDB3DF")
label.pack(pady=10)

bt_frame = tk.Frame(window, bg="#CDB3DF")
bt_frame.pack()

button1 = tk.Button(bt_frame, text="Login", command=login)
# button1.pack()
button1.grid(row=0, column=0, padx=10)

button2 = tk.Button(bt_frame, text="Register", command=register)
# button2.pack()
button2.grid(row=0, column=1)

label2 = tk.Label(window, text="Please access to the following URL and authorize to obtain the authorization code.")
label2.configure(bg="#CDB3DF")
label2.pack(pady=10)

button3 = tk.Button(window, text="Open URL", command=openURL)
button3.pack()

code_label = tk.Label(window, text="Authorization code:")
code_label.configure(bg="#CDB3DF")
code_label.pack(pady=10)

code = tk.Entry(window)
code.pack()

send_label = tk.Label(window, text="Thank you! Click the button and welcome to AHSC!")
send_label.configure(bg="#CDB3DF")
send_label.pack(pady=10)

send = tk.Button(window, text="Click Me!", command=get_token)
send.pack()

# close_label = tk.Label(window, text="Thank you! You can close now the window.")
# close_label.configure(bg="#CDB3DF")
# close_label.pack(pady=5)
#
# welcome_label = tk.Label(window, text="Welcome to AHSC!")
# welcome_label.configure(bg="#CDB3DF")
# welcome_label.pack(pady=5)

window.mainloop()