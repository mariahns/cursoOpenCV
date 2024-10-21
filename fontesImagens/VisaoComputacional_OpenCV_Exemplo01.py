import numpy as np
import cv2
# Load a color image in grayscale
img = cv2.imread('Visao_Computacional_Logo_Imagem.png',0)
assert img is not None, "Arquivo não encontrado!"
print(img.shape) # y,x
print(img.size)
cv2.imshow('OpenCV - GrayScale',img)
cv2.waitKey(5000)
# Load a color image 
img = cv2.imread('Visao_Computacional_Logo_Imagem.png',1)
print(img.shape)  # y,x,n
print(img.size)
cv2.imshow('OpenCV - Color',img)
cv2.waitKey(5000)
#Write image
cv2.imwrite("Visao_Computacional_Logo_Imagem_Copia.png", img)
cv2.destroyAllWindows()

