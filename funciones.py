# LIBRERIAS
import cv2 
import numpy as np

class Detector:

    count = 0

    def __init__(self):
        #Rango de colores HSV
        ## ROJO
        self.redBajo1 = np.array([0, 100, 20], np.uint8)
        self.redAlto1 = np.array([8, 255, 255], np.uint8)
        self.redBajo2 = np.array([175, 100, 20], np.uint8)
        self.redAlto2 = np.array([179, 255, 255], np.uint8)
        ## AZUL
        self.azulBajo = np.array([100, 100, 20], np.uint8)
        self.azulAlto = np.array([125, 255, 255], np.uint8)
        ## VERDE
        self.verdeBajo = np.array([40, 100, 20], np.uint8)
        self.verdeAlto = np.array([75, 255, 255], np.uint8)

    ## Funcion para Dibujar el contorno en la figura
    def dibujarContorno(self, cap, mask, color=(0,0,0)):
        contornos, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.count = self.count + len(contornos)
        for c in contornos:
            area = cv2.contourArea(c)
            if area > 3000:
                nuevoContorno = cv2.convexHull(c)
                cv2.drawContours(cap, [nuevoContorno], 0, color, 3)
                

    ## Funcion para usar video
    def video(self):
        try:
            #Inicializacion del cv2 para capturar video
            vip = cv2.VideoCapture(0)
            while True:
                ret,frame = vip.read()
                if ret==True:
                    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    maskAzul = cv2.inRange(frameHSV, self.azulBajo, self.azulAlto)
                    maskVerde = cv2.inRange(frameHSV, self.verdeBajo, self.verdeAlto)
                    maskRed1 = cv2.inRange(frameHSV, self.redBajo1, self.redAlto1)
                    maskRed2 = cv2.inRange(frameHSV, self.redBajo2, self.redAlto2)
                    maskRed = cv2.add(maskRed1, maskRed2)     
                    self.dibujarContorno(frame, maskAzul, (255,0,0)) 
                    self.dibujarContorno(frame, maskVerde, (0, 128, 0)) 
                    self.dibujarContorno(frame, maskRed, (0,0,255)) 
                    cv2.imshow('frame', frame)
                    if cv2.waitKey(1) & 0xFF == ord('s'):
                        break
            vip.release()
            cv2.destroyAllWindows()
        except:
            print("Ha ocurrido un erro inesperado")

    ## Funcion para usar imagen
    def imagen(self, img):
        try:
            #Inicializacion del cv2 para capturar imagen
            cap = cv2.imread(cv2.samples.findFile(img), cv2.IMREAD_COLOR)
            while True:
                frameHSV = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
                maskAzul = cv2.inRange(frameHSV, self.azulBajo, self.azulAlto)
                maskVerde = cv2.inRange(frameHSV, self.verdeBajo, self.verdeAlto)
                maskRed1 = cv2.inRange(frameHSV, self.redBajo1, self.redAlto1)
                maskRed2 = cv2.inRange(frameHSV, self.redBajo2, self.redAlto2)
                maskRed = cv2.add(maskRed1, maskRed2)     
                self.dibujarContorno(cap, maskAzul) 
                self.dibujarContorno(cap, maskVerde) 
                self.dibujarContorno(cap, maskRed) 
                cv2.imshow(img.split('/')[-1].split('.')[0], cap)
                if cv2.waitKey(0):
                    break
                cap.release()
                cv2.destroyAllWindows()
        except:
            print("Ha ocurrido un erro inesperado")
    
    def getCount(self):
        return self.count
