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

label = tk.Label(window, text="Hello! Please login or register in Freesound before using AHSC.")
label.configure(bg="#CDB3DF")
label.pack()

button1 = tk.Button(window, text="Login", command=login)
button1.pack()

button2 = tk.Button(window, text="Register", command=register)
button2.pack()

label2 = tk.Label(window, text="Please access to the following URL and authorize to obtain the authorization code.")
label2.configure(bg="#CDB3DF")
label2.pack()

button3 = tk.Button(window, text="Open URL", command=openURL)
button3.pack()

code_label = tk.Label(window, text="Authorization code:")
code_label.configure(bg="#CDB3DF")
code_label.pack()

code = tk.Entry(window)
code.pack()

send_label = tk.Label(window, text="Please click the button to send the token.")
send_label.configure(bg="#CDB3DF")
send_label.pack()

send = tk.Button(window, text="Send token", command=get_token)
send.pack()

close_label = tk.Label(window, text="Thank you! You can close now the window.")
close_label.configure(bg="#CDB3DF")
close_label.pack()

welcome_label = tk.Label(window, text="Welcome to AHSC!")
welcome_label.configure(bg="#CDB3DF")
welcome_label.pack()

window.mainloop()