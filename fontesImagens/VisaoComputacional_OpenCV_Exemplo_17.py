import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#img = cv2.imread('Grupo_Caxias_001.jpg')
#img = cv2.imread("Imagem_Pessoas_Juntas_001.jpg")
img = cv2.imread("Imagem_Pessoas_Juntas_002.jpg")

cv2.imshow('Original',img)
cv2.waitKey(0)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5) # Alterem para testar mais

for (x,y,w,h) in faces:    # Procura faces
 img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
 roi_gray = gray[y:y+h, x:x+w]
 roi_color = img[y:y+h, x:x+w]
 eyes = eye_cascade.detectMultiScale(roi_gray)
 for (ex,ey,ew,eh) in eyes:   # Procura olhos nas faces
     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
