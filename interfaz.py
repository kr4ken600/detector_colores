from tkinter import *
from tkinter import filedialog
from funciones import Detector

class Interfaz:
    def __init__(self, master):
        self.master = master
        master.title("Probando Interfaz")
        master.resizable(False, False)
        master.minsize(580,200)
        master.config({ 'background': '#E6DDC4'})

        self.etiqueta = Label(master, text="Detector de Colores")
        self.etiqueta.config(background="#E6DDC4", font=('Arial', 25))
        self.etiqueta.place(x=50, y=15)

        self.btnVideo = Button(master, text="Detectar colores mediante video", command=self.callVideo)
        self.btnVideo.place(x=50, y=85)
        self.btnVideo.config(font=('Arial', 11))

        self.btnImagen = Button(master, text="Detectar colores mediante imagen", command=self.browseFiles)
        self.btnImagen.place(x=300, y=85)
        self.btnImagen.config(font=('Arial', 11))

    def callVideo(self):
        video = Detector()
        video.video()

    def callImage(self, img):
        imagen = Detector()
        imagen.imagen(img)

        self.etiquetaCount = Label(self.master, text=f"Cantidad de Elementos Encontrados: {imagen.getCount()}")
        self.etiquetaCount.config(background="#E6DDC4", font=('Arial', 15))
        self.etiquetaCount.place(x=50, y=120)

    def browseFiles(self): 
        filename = filedialog.askopenfilename(title = "Selecciona la imagen" ,filetypes=[("Imagenes", ".jpg .png")]) 
        self.callImage(filename)

root = Tk()
test = Interfaz(root)
root.mainloop()