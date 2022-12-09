from tkinter import *
from tkinter import filedialog
from funciones import Detector

class Interfaz:
    def __init__(self, master):
        self.master = master
        master.title("Detector de Colores")
        master.resizable(False, False)
        master.minsize(580,200)
        master.config({ 'background': '#E6DDC4'})

        self.etiqueta = Label(master, text="Detector de Colores (Rojo, Azul, Verde)")
        self.etiqueta.config(background="#E6DDC4", font=('Arial', 25))
        self.etiqueta.place(x=5, y=15)

        self.btnVideo = Button(master, text="Detectar colores mediante video", command=self.callVideo)
        self.btnVideo.place(x=50, y=85)
        self.btnVideo.config(font=('Arial', 11))

        self.btnImagen = Button(master, text="Detectar colores mediante imagen", command=self.browseFiles)
        self.btnImagen.place(x=300, y=85)
        self.btnImagen.config(font=('Arial', 11))

        self.etiquetaBy = Label(master, text="By: Guzmán Guzmán Melanie Samantha")
        self.etiquetaBy.config(background="#E6DDC4", font=('Arial', 15))
        self.etiquetaBy.place(x=105, y=155)

    def callVideo(self):
        video = Detector()
        video.video()

    def callImage(self, img):
        imagen = Detector()
        imagen.imagen(img)

    def browseFiles(self): 
        filename = filedialog.askopenfilename(title = "Selecciona la imagen" ,filetypes=[("Imagenes", ".jpg .png")]) 
        self.callImage(filename)