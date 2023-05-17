import os
import tkinter as tk
from numpy.lib.user_array import container

screamingDir = "../program/testingSet/screaming"
owlDir = "../program/testingSet/owl"
carDir = "../program/testingSet/car engine"
knockingDir = "../program/testingSet/knocking"
rainDir = "../program/testingSet/rain"
ravenDir = "../program/testingSet/raven bird"
violinDir = "../program/testingSet/violin"

def showSounds(categoryDir):
    # Comprobar si el directorio existe
    if not os.path.isdir(categoryDir):
        print(f"El directorio '{categoryDir}' no existe.")
        return []

    # Obtener la lista de archivos y directorios en el directorio dado
    lista_elementos = os.listdir(categoryDir)

    # Filtrar solo las carpetas y añadirlas a la lista
    carpetas = [elemento for elemento in lista_elementos if os.path.isdir(os.path.join(categoryDir, elemento))]

    for sonido in carpetas:
        label = tk.Label(text=f"{sonido} - {categoryDir.split('/')[-1]}")
        label.pack()

def initGUI():
    window = tk.Tk()
    window.title("AHSC")
    window.geometry("1000x600")
    window.config(bg="#BE96EE")

    # Crear un contenedor principal
    main_frame = tk.Frame(window)
    main_frame.pack(fill=tk.BOTH)

    # Crear un lienzo (canvas)
    canvas = tk.Canvas(main_frame, bg="#BE96EE")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    label1 = tk.Label(master=main_frame, text="AHSC: Automatic Horror Sound Classification", bg="#9F64E6")
    label1.place(x=50, y=30)
    label1.config(font=('Arial', 15))

    frame2 = tk.Frame(master=canvas, height=10, bg="#BE96EE")
    frame2.pack(fill=tk.X)

    ######################################## BUTTONS ##############################################
    button_scream = tk.Button(frame2, text="Scream", command=lambda: showSounds(screamingDir))
    button_scream.pack()

    button_owl = tk.Button(canvas, text="Owl", command=lambda: showSounds(owlDir))
    button_owl.pack()

    button_car = tk.Button(canvas, text="Car engine", command=lambda: showSounds(carDir))
    button_car.pack()

    button_knocking = tk.Button(canvas, text="Knocking", command=lambda: showSounds(knockingDir))
    button_knocking.pack()

    button_rain = tk.Button(canvas, text="Rain", command=lambda: showSounds(rainDir))
    button_rain.pack()

    button_raven = tk.Button(canvas, text="Raven bird", command=lambda: showSounds(ravenDir))
    button_raven.pack()

    button_violin = tk.Button(canvas, text="Violin", command=lambda: showSounds(violinDir))
    button_violin.pack()

    window.mainloop()

#################### TO CALL THE GUI #################
initGUI()
