import cv2
import numpy as np

#Carregue a imagem de referência
img_ref = cv2.imread('referencia.png')

#Carregue a imagem de entrada
img_entrada = cv2.imread('entrada2.png')

#Defina o método de comparação e o limiar
method = cv2.TM_CCORR
threshold = 0.9

#Realize o template matching
result = cv2.matchTemplate(img_entrada, img_ref, method)

#Encontre os valores máximos acima do limiar
loc = np.where(result >= threshold)

#Desenhe retângulos ao redor das correspondências
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_entrada, pt, (pt[0] + img_ref.shape[1], pt[1] + img_ref.shape[0]), (0, 255, 0), 2)

#Exiba a imagem com as correspondências
cv2.imshow('Correspondências', img_entrada)
cv2.waitKey(0)
cv2.destroyAllWindows()
