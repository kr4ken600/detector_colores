# LIBRERIAS
import cv2 
import numpy as np
from sys import exit
from colorama import Fore, init

init()

#Rango de colores HSV
## ROJO
redBajo1 = np.array([0, 100, 20], np.uint8)
redAlto1 = np.array([8, 255, 255], np.uint8)
redBajo2 = np.array([175, 100, 20], np.uint8)
redAlto2 = np.array([179, 255, 255], np.uint8)
## AZUL
azulBajo = np.array([100, 100, 20], np.uint8)
azulAlto = np.array([125, 255, 255], np.uint8)
## VERDE
verdeBajo = np.array([40, 100, 20], np.uint8)
verdeAlto = np.array([75, 255, 255], np.uint8)

## Funcion para Dibujar el contorno en la figura
def dibujarContorno(cap, mask, color=(0,0,0)):
    contornos, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 3000:
            nuevoContorno = cv2.convexHull(c)
            cv2.drawContours(cap, [nuevoContorno], 0, color, 3)

## Funcion para usar video
def video():
    #Inicializacion del cv2 para capturar video
    vip = cv2.VideoCapture(0)
    while True:
        ret,frame = vip.read()
        if ret==True:
            frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            maskAzul = cv2.inRange(frameHSV, azulBajo, azulAlto)
            maskVerde = cv2.inRange(frameHSV, verdeBajo, verdeAlto)
            maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
            maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
            maskRed = cv2.add(maskRed1, maskRed2)     
            dibujarContorno(frame, maskAzul, (255,0,0)) 
            dibujarContorno(frame, maskVerde, (0, 128, 0)) 
            dibujarContorno(frame, maskRed, (0,0,255)) 
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
    vip.release()
    cv2.destroyAllWindows()

def imagen():
    #Inicializacion del cv2 para capturar imagen
    img = input('Agrega el nombre o direccion de la imagen: ') 
    cap = cv2.imread(cv2.samples.findFile(img + '.jpg'), cv2.IMREAD_COLOR)
    while True:
        frameHSV = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
        maskAzul = cv2.inRange(frameHSV, azulBajo, azulAlto)
        maskVerde = cv2.inRange(frameHSV, verdeBajo, verdeAlto)
        maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
        maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
        maskRed = cv2.add(maskRed1, maskRed2)     
        dibujarContorno(cap, maskAzul) 
        dibujarContorno(cap, maskVerde) 
        dibujarContorno(cap, maskRed) 
        cv2.imshow(img, cap)
        if cv2.waitKey(0):
            break
        cap.release()
        cv2.destroyAllWindows()

## Flujo del programa
if __name__ == '__main__':
    print(Fore.RED + '========= DETECTOR DE COLORES =========')
    print(Fore.BLUE +'*** By: Guzman Guzman Melanie Samantha ***\n\n')
    print(Fore.GREEN +'Mediante Video en Vivo => 1\n')
    print(Fore.GREEN +'Mediante una Imagen => 2\n')
    option = int(input(Fore.CYAN +'Selecciona una opcion: '))

    if option == 1:
        video()
    elif option == 2:
        imagen()
    else:
        print('Opcion no valida...')
        exit(1)