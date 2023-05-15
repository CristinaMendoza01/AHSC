import tkinter as tk

window = tk.Tk()
window.title("AHSC")
window.geometry("1000x600")
window.config(bg="#BE96EE")

frame1 = tk.Frame(master=window, height=100, bg="#9F64E6")
frame1.pack(fill=tk.X)
label1 = tk.Label(master=frame1, text="AHSC: Automatic Horror Sound Classification", bg="#9F64E6")
label1.place(x=80, y=30)
label1.config(font=('Arial', 15))

window.mainloop()